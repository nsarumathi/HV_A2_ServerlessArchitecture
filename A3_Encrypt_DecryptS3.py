import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Get all buckets
    buckets = s3.list_buckets()

    unencrypted_buckets = []

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']

        try:
            # Check encryption configuration
            s3.get_bucket_encryption(Bucket=bucket_name)
        except s3.exceptions.ClientError as e:
            error_code = e.response['Error']['Code']

            # If no encryption found
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                unencrypted_buckets.append(bucket_name)

    # Logging
    if unencrypted_buckets:
        print("Unencrypted Buckets:")
        for b in unencrypted_buckets:
            print(b)
    else:
        print("All buckets have encryption enabled")

    return {
        'statusCode': 200,
        'body': f"Found {len(unencrypted_buckets)} unencrypted buckets"
    }