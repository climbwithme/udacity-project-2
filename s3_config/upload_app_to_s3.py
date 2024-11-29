import boto3
import os
import argparse

def get_bucket_name(environment_name, region):
    """
    Retrieve the S3 bucket name from CloudFormation stack outputs.
    """
    cf_client = boto3.client('cloudformation', region_name=region)
    export_name = f"{environment_name}-S3BucketName"
    
    # Get all exports and filter for the specific bucket export
    exports = cf_client.list_exports()
    for export in exports['Exports']:
        if export['Name'] == export_name:
            return export['Value']
    
    raise ValueError(f"Bucket name not found for export: {export_name}")

def upload_files_to_s3(local_folder, bucket_name, region):
    """
    Upload all files from a local folder to the specified S3 bucket.
    """
    s3_client = boto3.client('s3', region_name=region)
    
    for root, _, files in os.walk(local_folder):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, local_folder)  # Relative path as S3 key
            print(f"Uploading {file_path} to s3://{bucket_name}/{s3_key}...")
            s3_client.upload_file(file_path, bucket_name, s3_key)
    print(f"All files from {local_folder} uploaded to bucket: {bucket_name}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Upload files to S3 bucket from a local folder.")
    parser.add_argument("environment_name", type=str, help="Environment name used to retrieve the S3 bucket")
    parser.add_argument("region", type=str, help="AWS region where the stack is deployed")
    parser.add_argument("local_folder", type=str, help="Local folder containing files to upload")
    args = parser.parse_args()

    try:
        # Retrieve the bucket name from CloudFormation output
        bucket_name = get_bucket_name(args.environment_name, args.region)
        print(f"Bucket name retrieved: {bucket_name}")
        
        # Upload files to the S3 bucket
        upload_files_to_s3(args.local_folder, bucket_name, args.region)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
