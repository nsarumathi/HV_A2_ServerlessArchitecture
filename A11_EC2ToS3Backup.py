import boto3
import datetime

ssm = boto3.client('ssm')
s3 = boto3.client('s3')

INSTANCE_ID = "i-0cff89fa2583f0f55"
BUCKET_NAME = "backupbucketsample1"
FOLDER_TO_BACKUP = "/home/ec2-user/data"

def lambda_handler(event, context):
    
    # 1. Create backup filename
    date_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    zip_file = f"/tmp/backup-{date_str}.zip"
    
    # 2. SSM command to zip + upload
    commands = [
        f"zip -r {zip_file} {FOLDER_TO_BACKUP}",
        f"aws s3 cp {zip_file} s3://{BUCKET_NAME}/"
    ]
    
    response = ssm.send_command(
        InstanceIds=[INSTANCE_ID],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': commands},
    )
    
    print("Backup command sent:", response)
    
    # 3. Delete files older than 30 days
    delete_old_backups()
    
    return "Backup + Cleanup completed"


def delete_old_backups():
    objects = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    if 'Contents' not in objects:
        return
    
    for obj in objects['Contents']:
        last_modified = obj['LastModified']
        age = datetime.datetime.now(last_modified.tzinfo) - last_modified
        
        if age.days > 30:
            print(f"Deleting {obj['Key']}")
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])