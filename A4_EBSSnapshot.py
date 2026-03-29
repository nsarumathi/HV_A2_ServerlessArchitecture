import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volume_id = 'vol-0646b4fdb953c2632'  

    # 🔹 Create snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description='Automated snapshot by Lambda'
    )

    snapshot_id = snapshot['SnapshotId']
    print(f"Created snapshot: {snapshot_id}")

    # 🔹 Define 30-day threshold
    threshold_date = datetime.now(timezone.utc) - timedelta(days=30)

    # 🔹 Get all snapshots owned by you
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])

    deleted_snapshots = []

    for snap in snapshots['Snapshots']:
        start_time = snap['StartTime']
        snap_id = snap['SnapshotId']

        # Delete snapshots older than 30 days
        if start_time < threshold_date:
            ec2.delete_snapshot(SnapshotId=snap_id)
            deleted_snapshots.append(snap_id)

    # 🔹 Logging
    if deleted_snapshots:
        print("Deleted snapshots:")
        for ds in deleted_snapshots:
            print(ds)
    else:
        print("No old snapshots to delete")

    return {
        'statusCode': 200,
        'body': f"Created {snapshot_id}, Deleted {len(deleted_snapshots)} old snapshots"
    }