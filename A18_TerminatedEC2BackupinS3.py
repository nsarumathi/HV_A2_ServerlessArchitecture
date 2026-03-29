import boto3
import json
from datetime import datetime

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

BUCKET_NAME = 'ec2-backup-bucketdemo'  

def lambda_handler(event, context):

    try:
        # -----------------------------
        # 1. GET INSTANCE ID FROM EVENT
        # -----------------------------
        instance_id = event['detail']['instance-id']
        print(f"Instance terminating: {instance_id}")

        # -----------------------------
        # 2. GET INSTANCE DETAILS
        # -----------------------------
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        volumes = []

        # -----------------------------
        # 3. GET ATTACHED VOLUMES
        # -----------------------------
        for mapping in instance['BlockDeviceMappings']:
            volume_id = mapping['Ebs']['VolumeId']
            volumes.append(volume_id)

        snapshot_ids = []

        # -----------------------------
        # 4. CREATE SNAPSHOTS
        # -----------------------------
        for vol in volumes:
            snap = ec2.create_snapshot(
                VolumeId=vol,
                Description=f"Backup before termination - {instance_id}"
            )
            snapshot_ids.append(snap['SnapshotId'])

        print(f"Snapshots created: {snapshot_ids}")

        # -----------------------------
        # 5. SAVE METADATA TO S3
        # -----------------------------
        backup_data = {
            "InstanceId": instance_id,
            "Time": str(datetime.utcnow()),
            "Volumes": volumes,
            "Snapshots": snapshot_ids
        }

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=f"{instance_id}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json",
            Body=json.dumps(backup_data),
            ContentType='application/json'
        )

        return {
            "status": "SUCCESS",
            "instance": instance_id,
            "snapshots": snapshot_ids
        }

    except Exception as e:
        print(str(e))
        return {
            "status": "FAILED",
            "error": str(e)
        }