import boto3
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

def empty_bucket(bucket_name, region):
    """
    Empty all objects and versions (if versioning is enabled) from the specified S3 bucket.
    """
    s3_client = boto3.client('s3', region_name=region)
    s3_resource = boto3.resource('s3', region_name=region)
    bucket = s3_resource.Bucket(bucket_name)
    
    # Delete all objects
    print(f"Deleting objects in bucket: {bucket_name}")
    bucket.objects.delete()
    
    # Delete all object versions if versioning is enabled
    print(f"Checking for object versions in bucket: {bucket_name}")
    bucket.object_versions.delete()

    print(f"Bucket {bucket_name} is now empty.")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Empty an S3 bucket.")
    parser.add_argument("environment_name", type=str, help="Environment name used to retrieve the S3 bucket")
    parser.add_argument("region", type=str, help="AWS region where the stack is deployed")
    args = parser.parse_args()

    try:
        # Retrieve the bucket name from CloudFormation output
        bucket_name = get_bucket_name(args.environment_name, args.region)
        print(f"Bucket name retrieved: {bucket_name}")
        
        # Empty the S3 bucket
        empty_bucket(bucket_name, args.region)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
