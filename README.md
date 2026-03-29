Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
------------------------------------------------------------------------------------
    Objective:Automatically manage EC2 instances (start/stop) based on tags.
    Key Steps:
    
       > Launch two EC2 instances (Auto-Stop and Auto-Start tags).
        
  <img width="1918" height="822" alt="Assg1_EC1" src="https://github.com/user-attachments/assets/677427a6-e183-4732-86f5-b3ada4df23cd" />
  <img width="1918" height="822" alt="Assg1_EC2" src="https://github.com/user-attachments/assets/d9bf6c0c-5403-44df-8d9d-cf25e6043552" />
  
       > Create a Lambda function with AmazonEC2FullAccess Role.
        
  <img width="1918" height="800" alt="Assgn1_Role" src="https://github.com/user-attachments/assets/d78ffc5a-433d-48db-b92b-3877058c855b" />

       > Use Boto3 to detect tagged instances and start/stop them.
        
  <img width="1918" height="866" alt="Assgn1_TestRun" src="https://github.com/user-attachments/assets/adee6653-a824-4c64-8b6d-f8e691b3d18b" />

       > Manually invoke Lambda and verify instance states.
        
  <img width="1918" height="802" alt="Assg1_EC2AfterRun" src="https://github.com/user-attachments/assets/0e0f0778-0ded-4dfd-951b-a5cef4fbe8d7" />

        
Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
--------------------------------------------------------------------------------------
    Objective: Delete S3 objects older than 30 days automatically.
    Key Steps:
    
     > Create an S3 bucket and upload test files.
<img width="1913" height="868" alt="Assgn2_S3Bucket" src="https://github.com/user-attachments/assets/11e20305-34a0-41bc-b77b-24e91574d423" />

     > Lambda function with AmazonS3FullAccess.
<img width="1918" height="867" alt="Assgn2_Rolepermission" src="https://github.com/user-attachments/assets/9460ffac-1802-443c-8cd8-2579d0ec4779" />

     > Use Boto3 to delete objects older than 30 days.
<img width="1917" height="863" alt="Assgn2_LmbdaExecution" src="https://github.com/user-attachments/assets/cd901d7d-4dec-4c76-8606-8a7501154bbc" />

     > Manually invoke Lambda to confirm cleanup.
<img width="1918" height="867" alt="Assgn2_s3Afterlambda" src="https://github.com/user-attachments/assets/3f4d1663-7241-4056-b382-3fb73d19170a" />

      
Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
----------------------------------------------------------------------------------------
    Objective: Detect S3 buckets without server-side encryption.
    Key Steps:
    
     > Create S3 buckets.
     
<img width="1918" height="826" alt="Assgn3_TwoBuckets_Bothencrypted" src="https://github.com/user-attachments/assets/2db7b0cd-068c-46a5-8f4b-c8b379c241ff" />

     > Lambda function with AmazonS3ReadOnlyAccess.
     
<img width="1918" height="867" alt="Assgn2_Rolepermission" src="https://github.com/user-attachments/assets/ab653f9b-0dba-47ea-9ee8-95f503d24c37" />

    > List buckets and log unencrypted ones.
    > Check Lambda logs to confirm detection.
    
<img width="1918" height="870" alt="Assgn3_EncryptedBuckets" src="https://github.com/user-attachments/assets/a7932b0d-0a1d-4c4a-a27b-e1497b498cb5" />

Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3
----------------------------------------------------------------------------------
    Objective: Automate EBS snapshots and delete snapshots older than 30 days.
    Key Steps:
    
     > Identify EBS volumes to back up.
     
<img width="1918" height="826" alt="Assgnment4_ebs" src="https://github.com/user-attachments/assets/6134cd26-c758-4355-9ec1-5a4de4502c4e" />

     > Lambda function with EC2 permissions.
     > Create new snapshots and delete old ones via Boto3.
     
<img width="1918" height="871" alt="Assgn4_Snapshots" src="https://github.com/user-attachments/assets/2b9a2215-50ea-423d-ab5d-9ad1146f6ae9" />

     > Optional: Schedule function using CloudWatch Events.
     
<img width="1918" height="870" alt="Assgn4_Trigger" src="https://github.com/user-attachments/assets/89b98145-01f7-47ec-a0d5-166779893d16" />
<img width="1918" height="863" alt="Assgn4_SnapshotbyTrigger" src="https://github.com/user-attachments/assets/02557480-90a8-4128-ae95-a7878f5403ba" />
    
Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3
-----------------------------------------------------------------------------------
    Objective: Automatically tag newly launched EC2 instances.
    Key Steps:
    
<img width="1918" height="866" alt="Assgn5_EC1" src="https://github.com/user-attachments/assets/41fed0a3-cbc7-4055-b8fc-da01ecc4c18a" />

     > Lambda triggers on instance launch.
     
<img width="1918" height="867" alt="Assg5_Eventriggr2" src="https://github.com/user-attachments/assets/fca655d8-d410-4ad6-8e07-5c49253d7c12" />

     > Apply tags including current date and custom info.
     > Verify automatic tagging on new instances.
     
<img width="1918" height="862" alt="Assgn5_Ec3" src="https://github.com/user-attachments/assets/2adc21bc-28c2-48d7-8bfe-15be8277ec74" />
<img width="1918" height="836" alt="Assgn5_ec2" src="https://github.com/user-attachments/assets/88d0a360-e3d8-4b95-acb8-f29875e36311" />

      
Assignment 6: Monitor and Alert High AWS Billing Using AWS Lambda, Boto3, and SNS
---------------------------------------------------------------------------------------
    Objective: Alert via SNS if AWS billing exceeds threshold.
    Key Steps:
    
     > Create SNS topic and subscribe email.
<img width="1918" height="650" alt="assgn6_snssubs" src="https://github.com/user-attachments/assets/b816cdaa-14f5-43da-845d-555beae6c238" />
<img width="1918" height="872" alt="Assgn6_Roleperm" src="https://github.com/user-attachments/assets/aac6d999-9960-4d62-8807-b885a4ba67f6" />

     > Lambda fetches billing metrics and checks threshold.
<img width="1918" height="871" alt="Assgn6_RegionBilling" src="https://github.com/user-attachments/assets/ce203fcb-bee1-4ce6-b7b6-828238a8bb70" />

     > Send notification if exceeded.
<img width="1918" height="971" alt="Assgn6_BillingEmail" src="https://github.com/user-attachments/assets/1dd11b27-d344-452f-9fe1-3c13d1fe6688" />

     > Schedule daily checks via CloudWatch Events.
<img width="1918" height="865" alt="Assign6_billingalert" src="https://github.com/user-attachments/assets/f9199050-0466-4051-b9d6-f392b2ed7054" />

      
Assignment 7: DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS
----------------------------------------------------------------------------------------
    Objective: Alert when a DynamoDB table item changes.
    Key Steps:
    
      > Create Table with items
    
<img width="1915" height="862" alt="assgn7_changestatus" src="https://github.com/user-attachments/assets/8a1740e9-cf36-4b12-8528-36f845d55f5f" />
      > Enable DynamoDB Streams.
      
<img width="1918" height="548" alt="assignmnt7_DBSTREam" src="https://github.com/user-attachments/assets/908028ae-3d62-4892-a215-8407a0341f9e" />

    > Lambda triggers on item change and sends SNS alert.
<img width="1917" height="871" alt="Asgn7_dynaodbtrigger" src="https://github.com/user-attachments/assets/8c7eb18b-92c2-429c-93cd-2ac35cdc6a15" />

<img width="1918" height="665" alt="assgn7_sns" src="https://github.com/user-attachments/assets/49d3f303-444a-4c2c-8596-937c9e6756ad" />

      > Verify notifications on item updates.
<img width="1918" height="872" alt="Assgn7_email" src="https://github.com/user-attachments/assets/3e33a43d-15c0-429f-bfbe-458490d0e5b7" />

      
Assignment 8: Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend
-------------------------------------------------------------------------------------------------
    Objective: Analyze sentiment using Amazon Comprehend.
    Key Steps:
    
    > Lambda receives reviews as input.
<img width="1918" height="863" alt="Assign8_IAMRole" src="https://github.com/user-attachments/assets/97136de5-fab8-49b7-afe8-df8f46d68750" />

    > Analyze sentiment and log result.
<img width="1918" height="812" alt="Assignmnt8_positivereview" src="https://github.com/user-attachments/assets/32efd5d8-e05f-4048-b700-cb75d2d4fa8c" />

<img width="1918" height="867" alt="Assgnmnt8_cloudwatch1" src="https://github.com/user-attachments/assets/0d0e3105-a325-421c-8bb3-8a0a76b280fd" />

    > Manual testing with sample reviews.
<img width="1918" height="862" alt="Assgn8_CloudwatchDetails" src="https://github.com/user-attachments/assets/411dbb6c-58d5-408d-b247-4bb3462d06d5" />

Assignment 9: Archive Old Files from S3 to Glacier Using AWS Lambda and Boto3
------------------------------------------------------------------------------------------------
    Objective: Move files older than 6 months to Glacier.
    Key Steps:
    
      > Identify old S3 objects.
      > Change storage class to Glacier via Lambda.
      
<img width="1918" height="821" alt="Assignment9_afterlambda" src="https://github.com/user-attachments/assets/8522adef-ab9e-4f4e-9515-cc3e6122e1c0" />

      > Log archived files for verification.
      
<img width="1918" height="681" alt="Asgnmnet9_S3Bucket" src="https://github.com/user-attachments/assets/2b118a0b-80a4-4ad3-861b-00e791c64075" />

Assignment 10: Notify When ELB 5xx Errors Spike Using AWS Lambda, Boto3, and SNS
-------------------------------------------------------------------------------------------------
    Objective: Receive alerts on high ELB 5xx errors.
    Key Steps:
    
     >  Lambda monitors 5xx errors.
<img width="1918" height="871" alt="Assg10_TG" src="https://github.com/user-attachments/assets/cbef708d-e0a1-4dd6-94bc-a799d9964ec0" />
<img width="1918" height="870" alt="Assg10_LB" src="https://github.com/user-attachments/assets/d7a2ddb8-f0f5-4f87-a62b-73eb572d5088" />

     >  Send SNS alert if threshold exceeded.
<img width="1918" height="860" alt="assgn10_sns" src="https://github.com/user-attachments/assets/42ebedfc-4018-479a-8b3e-9ba40b30d2a7" />

     >  Schedule Lambda every 5 minutes.
<img width="1918" height="867" alt="Assgn10_LambdaTrigger" src="https://github.com/user-attachments/assets/6bb29fbe-1f2b-457c-b800-e98d01c865ca" />


Assignment 11: EC2 Backup and File Cleanup Using Lambda, Boto3, and S3
--------------------------------------------------------------------------------------------------
    Objective: Backup EC2 files to S3 and delete old backups.
    Key Steps:
    
<img width="1913" height="867" alt="A11_EC2" src="https://github.com/user-attachments/assets/381f1626-2a20-4315-955a-2245193f5f61" />
<img width="1918" height="528" alt="A11_role+ec2" src="https://github.com/user-attachments/assets/b12fec9b-9b83-465e-9336-52f662e977a4" />
<img width="1918" height="870" alt="A11_Fleet" src="https://github.com/user-attachments/assets/913fbefb-45d8-4cea-b80a-e5cd70e86097" />

     > Lambda zips files from EC2 and uploads to S3.
     
<img width="1918" height="863" alt="A11_S3Bucket" src="https://github.com/user-attachments/assets/280d04e9-631f-4ee2-9aba-adf33e578fc5" />
<img width="1918" height="867" alt="A11_TestOp" src="https://github.com/user-attachments/assets/2937dce9-ad8d-4a95-8052-ad4929e55586" />

     > Delete backups older than 30 days.
     > Schedule daily via CloudWatch Events
     
<img width="1918" height="832" alt="A11-LOGS" src="https://github.com/user-attachments/assets/8bf37f6a-65af-4844-b1c6-41439c402122" />
<img width="1918" height="873" alt="A11_S3Backup" src="https://github.com/user-attachments/assets/41765086-c7c1-42b4-ab0e-580406d7f0e7" />

      
Assignment 12: Auto-Scale EC2 Instances Based on Load Using AWS Lambda, Boto3, and SNS
--------------------------------------------------------------------------------------------------
    Objective: Automatically scale EC2 instances based on ELB network load.
    Key Steps:
    
     > Monitor network load via Lambda.
     
<img width="1918" height="866" alt="A12_EC2" src="https://github.com/user-attachments/assets/a62c38aa-6e31-4257-b2f7-c26a9b05548c" />
<img width="1918" height="870" alt="A12_TG" src="https://github.com/user-attachments/assets/bf295880-497b-4173-a24b-671154f5665b" />
<img width="1918" height="862" alt="A12_LB" src="https://github.com/user-attachments/assets/2ea8ef2f-93d4-45ca-9490-d031570e486d" />

 ScaleDown:

<img width="1918" height="743" alt="A12_Autoscaledown" src="https://github.com/user-attachments/assets/dd6bf0fd-588e-4733-95a6-516d028e4f44" />
<img width="1917" height="427" alt="A12_ScaleDownEc" src="https://github.com/user-attachments/assets/4996d311-7bbc-4f4f-9363-2d61cdf741cd" />

     > Launch or terminate instances based on thresholds.
     
<img width="1918" height="462" alt="A12_ec2scaleup" src="https://github.com/user-attachments/assets/cdaee4ef-a835-4a64-bcfe-935c33103145" />

     > Notify via SNS.
     
<img width="1918" height="868" alt="A12_SNS" src="https://github.com/user-attachments/assets/303132be-7c4d-4846-9914-269c01779a29" />

     > Schedule function every 5 minutes.
     
<img width="1917" height="702" alt="A12_EMailNotification" src="https://github.com/user-attachments/assets/74b3100e-8e0a-4df0-b9e3-3e850c53be50" />

Assignment 13: Audit S3 Bucket Permissions and Notify for Public Buckets
--------------------------------------------------------------------------------------------------
    Objective: Alert if buckets have public access.
    Key Steps:
    
     > Check bucket permissions.
<img width="1918" height="782" alt="A13_S3_Public" src="https://github.com/user-attachments/assets/850a8cb4-42d3-4a03-b4a5-d347e9eca736" />

     > Send SNS alert if public read/write access detected.
<img width="1918" height="861" alt="A13_LambdaAfter" src="https://github.com/user-attachments/assets/ee82d58a-4e63-4d61-af5f-18d4e9a164b1" />

<img width="1918" height="732" alt="A13_Sns" src="https://github.com/user-attachments/assets/219f0972-e207-4e1a-8bfe-6df912697fa3" />

     > Schedule daily audit.
<img width="1918" height="683" alt="A13_EmailAlert" src="https://github.com/user-attachments/assets/c7de624e-fa3a-4612-8c7c-f620fd249314" />


Assignment 14: Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS
--------------------------------------------------------------------------------------------------
    Objective: Alert on EC2 state changes (start/stop).
    Key Steps:
    
     > Lambda triggers on instance state change.
     
<img width="1918" height="822" alt="A14_RolePer" src="https://github.com/user-attachments/assets/cf550f2c-3e53-4af9-886c-1a2f0c45e75e" />
<img width="1918" height="865" alt="A14_EventTrigger" src="https://github.com/user-attachments/assets/a7d7bb31-0031-419a-b411-af639ebf9da0" />

     > Send SNS notification with instance details.
     
<img width="1918" height="686" alt="A14_sns" src="https://github.com/user-attachments/assets/9baa3de6-8871-4532-9e76-10ca4b3d75b7" />

     > Test by starting/stopping instances.
     
<img width="1918" height="868" alt="A14_eMAILaLERT" src="https://github.com/user-attachments/assets/95daed45-d8b7-401e-aa7b-ff3d958575e4" />

Assignment 15: Implement a Log Cleaner for S3
--------------------------------------------------------------------------------------------------
    Objective: Delete logs older than 90 days from S3.
    Key Steps:
    
<img width="1918" height="737" alt="A15_S3Bucket" src="https://github.com/user-attachments/assets/bf1a2fa2-5ceb-4573-a278-0d7dc8b9285e" />

     > Lambda lists log files and deletes old ones.
<img width="1918" height="868" alt="A15_LogcleanerbyLatest" src="https://github.com/user-attachments/assets/d47233cb-8249-4191-8511-e4a0f1a1c1a8" />
<img width="1637" height="573" alt="A15_S3AfterRun" src="https://github.com/user-attachments/assets/6944c473-2611-44b5-8c5b-d87a81422ae3" />

     > Schedule weekly cleanup via EventBridge.
<img width="1918" height="867" alt="A15_EventTRigger" src="https://github.com/user-attachments/assets/2646101f-5618-402c-8479-c5f69edc1a3a" />


Assignment 16: Automated SNS Alerts for EC2 Disk Space Utilization
--------------------------------------------------------------------------------------------------
    Objective: Notify if EC2 disk usage exceeds 85%.
    Key Steps:
    
     > Lambda checks disk space.
<img width="1918" height="862" alt="A16_CloudwatchCWAgent" src="https://github.com/user-attachments/assets/b63ece1a-b25b-49ef-a35f-7dde9a44d582" />

     > Publish SNS alert if threshold exceeded.
<img width="1918" height="737" alt="A16_SNS" src="https://github.com/user-attachments/assets/86c1915f-e9ed-46ec-b28b-11f6efa4c05d" />

     > Schedule daily via CloudWatch Events.

Assignment 17: Restore EC2 Instance from Snapshot
--------------------------------------------------------------------------------------------------
    Objective: Create a new EC2 instance from the latest snapshot.
    Key Steps:
    
      > Fetch the latest snapshot.
<img width="1918" height="473" alt="A17_EC2Snap1" src="https://github.com/user-attachments/assets/9f5c29d3-9b8b-455f-a19d-bc6256b33f78" />
<img width="1917" height="862" alt="A17-EC2Snap2" src="https://github.com/user-attachments/assets/b6821dce-1763-431c-8cc5-a8858c3b7ac9" />

      > Launch new instance from snapshot.
<img width="1918" height="871" alt="A17_snap2EC" src="https://github.com/user-attachments/assets/7ab778f3-f73e-484e-8e6d-1f3478a5076a" />

      > Trigger manually or schedule.
<img width="1918" height="461" alt="A17_EC2List" src="https://github.com/user-attachments/assets/2f47cce9-db63-4150-87f4-742b624479f4" />

Assignment 18: Autosave EC2 Instance State Before Shutdown
--------------------------------------------------------------------------------------------------
    Objective: Save EC2 instance state before termination.
    Key Steps:
    
     > Create S3 Bucket
<img width="1918" height="591" alt="A18_S3bucket" src="https://github.com/user-attachments/assets/e176466b-32eb-4977-bfbf-d039662966ce" />

     > Detect instance termination event.
<img width="1918" height="827" alt="A18_EC2SSS" src="https://github.com/user-attachments/assets/873a16cf-90ae-4727-a3f7-3b71ba6139c2" />

     > Save files/state to S3.
<img width="1918" height="675" alt="A18_MetaddateinS3" src="https://github.com/user-attachments/assets/66d2bc48-80b4-4016-99de-82a57d0ea2c3" />

     > Trigger Lambda on termination events.
<img width="1918" height="835" alt="A18_EventTrigger" src="https://github.com/user-attachments/assets/ccacc847-6228-4992-902a-9d445fce7fa9" />


Assignment 19: Load Balancer Health Checker
--------------------------------------------------------------------------------------------------
    Objective: Monitor ELB health and alert if instances are unhealthy.
    Key Steps:
    
     > Check registered instance health behind ELB.
     > Send SNS notification if any instance is unhealthy.
<img width="1917" height="680" alt="A19_SNS" src="https://github.com/user-attachments/assets/97afa27c-86eb-4478-bd2b-901cad000953" />

     > Schedule Lambda to run every 10 minutes.
     
<img width="1918" height="802" alt="A19_EventTrigger" src="https://github.com/user-attachments/assets/fcd085f9-92f0-4038-a864-9ae68bffd13e" />
<img width="1918" height="866" alt="A19_ManualTrigger" src="https://github.com/user-attachments/assets/b816c776-7237-4e70-ba98-3b78da432018" />
<img width="1918" height="873" alt="A19_Emailnotif" src="https://github.com/user-attachments/assets/1b6c5b95-bc96-4689-9a3f-973e6e74fc9a" />
