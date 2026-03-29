import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get instances with Auto-Stop tag
    stop_instances = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    # Extract instance IDs
    stop_ids = []
    for reservation in stop_instances['Reservations']:
        for instance in reservation['Instances']:
            stop_ids.append(instance['InstanceId'])

    # Stop instances
    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print(f"Stopping instances: {stop_ids}")
    else:
        print("No instances to stop")

    # Get instances with Auto-Start tag
    start_instances = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    # Extract instance IDs
    start_ids = []
    for reservation in start_instances['Reservations']:
        for instance in reservation['Instances']:
            start_ids.append(instance['InstanceId'])

    # Start instances
    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print(f"Starting instances: {start_ids}")
    else:
        print("No instances to start")

    return {
        'statusCode': 200,
        'body': 'EC2 instance management completed'
    }