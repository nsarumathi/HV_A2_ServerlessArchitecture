import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = 'my-archive-bucket1'

# 🔥 1 minute threshold for testing
AGE_THRESHOLD = timedelta(minutes=1)


def is_older_than_threshold(last_modified):
    cutoff_date = datetime.now(timezone.utc) - AGE_THRESHOLD
    return last_modified < cutoff_date


def move_to_glacier(bucket, key):
    try:
        s3.copy_object(
            Bucket=bucket,
            Key=key,
            CopySource={'Bucket': bucket, 'Key': key},
            StorageClass='GLACIER',
            MetadataDirective='COPY'
        )
        print(f"Archived to Glacier: {key}")

    except Exception as e:
        print(f"Failed to archive {key}: {str(e)}")


def lambda_handler(event, context):
    print("Lambda execution started")

    continuation_token = None
    archived_files = []

    try:
        while True:
            if continuation_token:
                response = s3.list_objects_v2(
                    Bucket=BUCKET_NAME,
                    ContinuationToken=continuation_token
                )
            else:
                response = s3.list_objects_v2(Bucket=BUCKET_NAME)

            if 'Contents' not in response:
                print("No objects found in bucket")
                break

            for obj in response['Contents']:
                key = obj['Key']
                last_modified = obj['LastModified']

                try:
                    if is_older_than_threshold(last_modified):
                        move_to_glacier(BUCKET_NAME, key)
                        archived_files.append(key)

                except Exception as inner_error:
                    print(f"Error processing {key}: {str(inner_error)}")

            # Pagination
            if response.get('IsTruncated'):
                continuation_token = response.get('NextContinuationToken')
            else:
                break

        print("Lambda execution completed")
        print(f"Total archived files: {len(archived_files)}")

        return {
            "statusCode": 200,
            "body": f"Archived {len(archived_files)} files"
        }

    except Exception as e:
        print("Critical error:", str(e))
        return {
            "statusCode": 500,
            "body": str(e)
        }