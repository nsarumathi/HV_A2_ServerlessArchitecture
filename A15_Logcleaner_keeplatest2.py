import boto3
from datetime import datetime, timezone

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket to clean
BUCKET_NAME = "backupbucketsample1"

# Number of most recent files to keep
FILES_TO_KEEP = 3

def lambda_handler(event, context):
    print(f"Starting cleanup for bucket: {BUCKET_NAME}")

    # List all objects in the bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    if 'Contents' not in response:
        print("No objects found in bucket.")
        return {"statusCode": 200, "body": "No objects found."}
    
    objects = response['Contents']
    
    # Sort objects by LastModified descending (newest first)
    objects_sorted = sorted(objects, key=lambda x: x['LastModified'], reverse=True)
    
    # Keep the latest FILES_TO_KEEP, delete the rest
    to_delete = objects_sorted[FILES_TO_KEEP:]
    
    deleted_files = []
    for obj in to_delete:
        key = obj['Key']
        s3.delete_object(Bucket=BUCKET_NAME, Key=key)
        deleted_files.append(key)
        print(f"Deleted: {key}")
    
    print(f"Total files deleted: {len(deleted_files)}")
    
    return {
        "statusCode": 200,
        "body": f"Deleted {len(deleted_files)} files. Kept {FILES_TO_KEEP} latest files."
    }