import boto3
import argparse
import json

def create_stack(client, stack_name, template_path, parameters_path):
    with open(template_path, 'r') as template_file:
        template_body = template_file.read()

    with open(parameters_path, 'r') as parameters_file:
        parameters = json.load(parameters_file)

    response = client.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(f"Stack creation initiated. Response: {response}")

def update_stack(client, stack_name, template_path, parameters_path):
    with open(template_path, 'r') as template_file:
        template_body = template_file.read()

    with open(parameters_path, 'r') as parameters_file:
        parameters = json.load(parameters_file)

    response = client.update_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(f"Stack update initiated. Response: {response}")

def delete_stack(client, stack_name):
    response = client.delete_stack(
        StackName=stack_name
    )
    print(f"Stack deletion initiated. Response: {response}")

def main():
    parser = argparse.ArgumentParser(description="AWS CloudFormation stack operations")
    parser.add_argument('action', choices=['create', 'update', 'delete'], help="Action to perform")
    parser.add_argument('--stack-name', required=True, help="Name of the CloudFormation stack")
    parser.add_argument('--template-path', help="Path to the CloudFormation template file")
    parser.add_argument('--parameters-path', help="Path to the parameters JSON file")

    args = parser.parse_args()

    # Ensure the region is set when creating the client
    client = boto3.client('cloudformation', region_name='us-east-1')

    if args.action == 'create':
        if not args.template_path or not args.parameters_path:
            print("Template path and parameters path are required for creating a stack.")
            return
        create_stack(client, args.stack_name, args.template_path, args.parameters_path)

    elif args.action == 'update':
        if not args.template_path or not args.parameters_path:
            print("Template path and parameters path are required for updating a stack.")
            return
        update_stack(client, args.stack_name, args.template_path, args.parameters_path)

    elif args.action == 'delete':
        delete_stack(client, args.stack_name)

if __name__ == '__main__':
    main()
