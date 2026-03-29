import boto3
from datetime import datetime, timezone, timedelta

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket to clean
BUCKET_NAME = "backupbucketsample1"

# Delete logs older than this many days
RETENTION_DAYS = 90

def lambda_handler(event, context):
    print(f"Starting log cleanup for bucket: {BUCKET_NAME}")
    
    # Calculate cutoff date
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
    
    # List all objects in the bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    if 'Contents' not in response:
        print("No objects found in bucket.")
        return
    
    deleted_files = []
    
    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']
        
        if last_modified < cutoff_date:
            # Delete object
            s3.delete_object(Bucket=BUCKET_NAME, Key=key)
            deleted_files.append(key)
            print(f"Deleted: {key}")
    
    print(f"Total files deleted: {len(deleted_files)}")
    
    return {
        "statusCode": 200,
        "body": f"Deleted {len(deleted_files)} files."
    }