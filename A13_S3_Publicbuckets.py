import boto3
import json

s3 = boto3.client('s3')
sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-2:944765969321:S3PublicBucketAlerts"

def is_bucket_public(bucket_name):
    try:
        # Check Bucket Policy Status (BEST WAY)
        policy_status = s3.get_bucket_policy_status(Bucket=bucket_name)
        if policy_status['PolicyStatus']['IsPublic']:
            return True

    except Exception:
        pass  # No policy or access issue

    try:
        # Check ACL (fallback)
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            grantee = grant.get('Grantee', {})
            permission = grant.get('Permission')

            if 'URI' in grantee:
                # Public group
                if "AllUsers" in grantee['URI'] or "AuthenticatedUsers" in grantee['URI']:
                    if permission in ['READ', 'WRITE', 'FULL_CONTROL']:
                        return True

    except Exception:
        pass

    return False


def lambda_handler(event, context):
    public_buckets = []

    # 1. List all buckets
    response = s3.list_buckets()
    buckets = response['Buckets']

    # 2. Check each bucket
    for bucket in buckets:
        bucket_name = bucket['Name']
        print(f"Checking bucket: {bucket_name}")

        if is_bucket_public(bucket_name):
            public_buckets.append(bucket_name)

    # 3. Send SNS Notification if any public bucket found
    if public_buckets:
        message = "🚨 Public S3 Buckets Detected:\n\n" + "\n".join(public_buckets)

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="S3 Security Alert: Public Buckets Found",
            Message=message
        )

        print("Notification sent!")
    else:
        print("No public buckets found.")

    return {
        "statusCode": 200,
        "body": json.dumps(public_buckets)
    }