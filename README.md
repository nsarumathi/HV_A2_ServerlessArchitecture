Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
------------------------------------------------------------------------------------
    Objective:Automatically manage EC2 instances (start/stop) based on tags.
    Key Steps:
    ~~~~~~~~~~~
        Launch two EC2 instances (Auto-Stop and Auto-Start tags).
  <img width="1918" height="822" alt="Assg1_EC1" src="https://github.com/user-attachments/assets/677427a6-e183-4732-86f5-b3ada4df23cd" />
  <img width="1918" height="822" alt="Assg1_EC2" src="https://github.com/user-attachments/assets/d9bf6c0c-5403-44df-8d9d-cf25e6043552" />
        Create a Lambda function with AmazonEC2FullAccess Role.
  <img width="1918" height="800" alt="Assgn1_Role" src="https://github.com/user-attachments/assets/d78ffc5a-433d-48db-b92b-3877058c855b" />

        Use Boto3 to detect tagged instances and start/stop them.
  <img width="1918" height="866" alt="Assgn1_TestRun" src="https://github.com/user-attachments/assets/adee6653-a824-4c64-8b6d-f8e691b3d18b" />

        Manually invoke Lambda and verify instance states.
  <img width="1918" height="802" alt="Assg1_EC2AfterRun" src="https://github.com/user-attachments/assets/0e0f0778-0ded-4dfd-951b-a5cef4fbe8d7" />

        
Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
--------------------------------------------------------------------------------------
    Objective: Delete S3 objects older than 30 days automatically.
    Key Steps:
      Create an S3 bucket and upload test files.
      Lambda function with AmazonS3FullAccess.
      Use Boto3 to delete objects older than 30 days.
      Manually invoke Lambda to confirm cleanup.
      
Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
----------------------------------------------------------------------------------------
    Objective: Detect S3 buckets without server-side encryption.
    Key Steps:
      Create S3 buckets (some unencrypted).
      Lambda function with AmazonS3ReadOnlyAccess.
      List buckets and log unencrypted ones.
      Check Lambda logs to confirm detection.
      
Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3
----------------------------------------------------------------------------------
    Objective: Automate EBS snapshots and delete snapshots older than 30 days.
    Key Steps:
      Identify EBS volumes to back up.
      Lambda function with EC2 permissions.
      Create new snapshots and delete old ones via Boto3.
      Optional: Schedule function using CloudWatch Events.
      
Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3
-----------------------------------------------------------------------------------
    Objective: Automatically tag newly launched EC2 instances.
    Key Steps:
      Lambda triggers on instance launch.
      Apply tags including current date and custom info.
      Verify automatic tagging on new instances.
      
Assignment 6: Monitor and Alert High AWS Billing Using AWS Lambda, Boto3, and SNS
---------------------------------------------------------------------------------------
    Objective: Alert via SNS if AWS billing exceeds threshold.
    Key Steps:
      Create SNS topic and subscribe email.
      Lambda fetches billing metrics and checks threshold.
      Send notification if exceeded.
      Schedule daily checks via CloudWatch Events.
      
Assignment 7: DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS
----------------------------------------------------------------------------------------
    Objective: Alert when a DynamoDB table item changes.
    Key Steps:
      Enable DynamoDB Streams.
      Lambda triggers on item change and sends SNS alert.
      Verify notifications on item updates.
      
Assignment 8: Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend
-------------------------------------------------------------------------------------------------
    Objective: Analyze sentiment using Amazon Comprehend.
    Key Steps:
      Lambda receives reviews as input.
      Analyze sentiment and log result.
      Manual testing with sample reviews.
      
Assignment 9: Archive Old Files from S3 to Glacier Using AWS Lambda and Boto3
------------------------------------------------------------------------------------------------
    Objective: Move files older than 6 months to Glacier.
    Key Steps:
      Identify old S3 objects.
      Change storage class to Glacier via Lambda.
      Log archived files for verification.
      
Assignment 10: Notify When ELB 5xx Errors Spike Using AWS Lambda, Boto3, and SNS
-------------------------------------------------------------------------------------------------
    Objective: Receive alerts on high ELB 5xx errors.
    Key Steps:
      Lambda monitors 5xx errors.
      Send SNS alert if threshold exceeded.
      Schedule Lambda every 5 minutes.

Assignment 11: EC2 Backup and File Cleanup Using Lambda, Boto3, and S3
--------------------------------------------------------------------------------------------------
    Objective: Backup EC2 files to S3 and delete old backups.
    Key Steps:
      Lambda zips files from EC2 and uploads to S3.
      Delete backups older than 30 days.
      Schedule daily via CloudWatch Events
      
Assignment 12: Auto-Scale EC2 Instances Based on Load Using AWS Lambda, Boto3, and SNS
--------------------------------------------------------------------------------------------------
    Objective: Automatically scale EC2 instances based on ELB network load.
    Key Steps:
      Monitor network load via Lambda.
      Launch or terminate instances based on thresholds.
      Notify via SNS.
      Schedule function every 5 minutes.
      
Assignment 13: Audit S3 Bucket Permissions and Notify for Public Buckets
--------------------------------------------------------------------------------------------------
    Objective: Alert if buckets have public access.
    Key Steps:
      Check bucket permissions.
      Send SNS alert if public read/write access detected.
      Schedule daily audit.

Assignment 14: Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS
--------------------------------------------------------------------------------------------------
    Objective: Alert on EC2 state changes (start/stop).
    Key Steps:
      Lambda triggers on instance state change.
      Send SNS notification with instance details.
      Test by starting/stopping instances.

Assignment 15: Implement a Log Cleaner for S3
--------------------------------------------------------------------------------------------------
    Objective: Delete logs older than 90 days from S3.
    Key Steps:
      Lambda lists log files and deletes old ones.
      Schedule weekly cleanup via EventBridge.

Assignment 16: Automated SNS Alerts for EC2 Disk Space Utilization
--------------------------------------------------------------------------------------------------
    Objective: Notify if EC2 disk usage exceeds 85%.
    Key Steps:
      Lambda checks disk space.
      Publish SNS alert if threshold exceeded.
      Schedule daily via CloudWatch Events.

Assignment 17: Restore EC2 Instance from Snapshot
--------------------------------------------------------------------------------------------------
    Objective: Create a new EC2 instance from the latest snapshot.
    Key Steps:
      Fetch the latest snapshot.
      Launch new instance from snapshot.
      Trigger manually or schedule.


Assignment 18: Autosave EC2 Instance State Before Shutdown
--------------------------------------------------------------------------------------------------
    Objective: Save EC2 instance state before termination.
    Key Steps:
      Detect instance termination event.
      Save files/state to S3.
      Trigger Lambda on termination events.

Assignment 19: Load Balancer Health Checker
--------------------------------------------------------------------------------------------------
    Objective: Monitor ELB health and alert if instances are unhealthy.
    Key Steps:
      Check registered instance health behind ELB.
      Send SNS notification if any instance is unhealthy.
      Schedule Lambda to run every 10 minutes.
