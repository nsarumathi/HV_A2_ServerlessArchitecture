import boto3
import time
from datetime import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    try:
        # -----------------------------
        # CONFIG (UPDATE THESE VALUES)
        # -----------------------------
        OWNER_ID = 'self'  
        INSTANCE_TYPE = 't3.micro'
        SUBNET_ID = 'subnet-052bdb03da2046813'        
        SECURITY_GROUP_ID = 'sg-059586966eb79f215'   
        KEY_NAME = 'demo'          

        # -----------------------------
        # 1. GET LATEST SNAPSHOT
        # -----------------------------
        snapshots = ec2.describe_snapshots(OwnerIds=[OWNER_ID])['Snapshots']

        if not snapshots:
            return {"status": "FAILED", "message": "No snapshots found"}

        latest_snapshot = sorted(
            snapshots,
            key=lambda x: x['StartTime'],
            reverse=True
        )[0]

        snapshot_id = latest_snapshot['SnapshotId']
        print(f"Latest Snapshot: {snapshot_id}")

        # -----------------------------
        # 2. CREATE AMI FROM SNAPSHOT
        # -----------------------------
        ami_name = f"auto-ami-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        response = ec2.register_image(
            Name=ami_name,
            Architecture='x86_64',
            RootDeviceName='/dev/xvda',
            VirtualizationType='hvm',
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'SnapshotId': snapshot_id,
                        'DeleteOnTermination': True,
                        'VolumeType': 'gp2'
                    }
                }
            ]
        )

        image_id = response['ImageId']
        print(f"AMI Created: {image_id}")

        # -----------------------------
        # 3. WAIT FOR AMI TO BE READY
        # -----------------------------
        print("Waiting for AMI to become available...")
        waiter = ec2.get_waiter('image_available')
        waiter.wait(ImageIds=[image_id])

        time.sleep(20)  # extra safety wait

        # -----------------------------
        # 4. LAUNCH EC2 INSTANCE
        # -----------------------------
        print("Launching EC2 instance...")

        instance = ec2.run_instances(
            ImageId=image_id,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            MinCount=1,
            MaxCount=1,
            SubnetId=SUBNET_ID,
            SecurityGroupIds=[SECURITY_GROUP_ID],
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'Recovered-Instance'}
                    ]
                }
            ]
        )

        instance_id = instance['Instances'][0]['InstanceId']
        print(f"Instance Launched: {instance_id}")

        return {
            "status": "SUCCESS",
            "SnapshotId": snapshot_id,
            "AMI": image_id,
            "InstanceId": instance_id
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "status": "FAILED",
            "error": str(e)
        }