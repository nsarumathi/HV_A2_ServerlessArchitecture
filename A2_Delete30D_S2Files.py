import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'assgndemobucket'

    # Define 30-day threshold
    threshold_date = datetime.now(timezone.utc) - timedelta(days=30)

    # List objects in bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("Bucket is empty")
        return

    deleted_files = []

    for obj in response['Contents']:
        object_key = obj['Key']
        last_modified = obj['LastModified']

        # Check if object is older than 30 days
        if last_modified < threshold_date:
            s3.delete_object(Bucket=bucket_name, Key=object_key)
            deleted_files.append(object_key)

    # Logging
    if deleted_files:
        print("Deleted files:")
        for file in deleted_files:
            print(file)
    else:
        print("No old files found")

    return {
        'statusCode': 200,
        'body': f"Deleted {len(deleted_files)} old files"
    }