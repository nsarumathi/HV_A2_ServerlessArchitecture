import boto3
import time
from datetime import datetime, timedelta

ssm = boto3.client('ssm')
s3 = boto3.client('s3')

INSTANCE_ID = 'i-0c07235c1264c0d2a'
BUCKET_NAME = 'backupbucketsample1'
FOLDER_TO_BACKUP = '/home/ec2-user/data'

def lambda_handler(event, context):
    
    # Step 1: Create backup via SSM
    timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
    zip_file = f"/tmp/backup-{timestamp}.zip"
    s3_key = f"backups/backup-{timestamp}.zip"

    commands = [
        f"zip -r {zip_file} {FOLDER_TO_BACKUP}",
        f"aws s3 cp {zip_file} s3://{BUCKET_NAME}/{s3_key}"
    ]

    response = ssm.send_command(
        InstanceIds=[INSTANCE_ID],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': commands},
    )

    command_id = response['Command']['CommandId']

    # Wait for command execution
    time.sleep(10)

    output = ssm.get_command_invocation(
        CommandId=command_id,
        InstanceId=INSTANCE_ID
    )

    print("Backup Status:", output['Status'])

    # Step 2: Delete old backups (30 days)
    delete_old_backups()

    return "Backup and cleanup completed"


def delete_old_backups():
    objects = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix='backups/')

    if 'Contents' not in objects:
        return

    for obj in objects['Contents']:
        if obj['LastModified'] < datetime.now(obj['LastModified'].tzinfo) - timedelta(days=30):
            print(f"Deleting {obj['Key']}")
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])