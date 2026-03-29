import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'assgndemobucket'  

    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("Bucket is already empty")
        return {
            'statusCode': 200,
            'body': 'No files to delete'
        }

    objects_to_delete = [{'Key': obj['Key']} for obj in response['Contents']]

    # Delete all objects
    s3.delete_objects(
        Bucket=bucket_name,
        Delete={'Objects': objects_to_delete}
    )

    print("Deleted files:")
    for obj in objects_to_delete:
        print(obj['Key'])

    return {
        'statusCode': 200,
        'body': f"Deleted {len(objects_to_delete)} files"
    }