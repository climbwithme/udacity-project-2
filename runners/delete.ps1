param(
    [string]$StackName
)

aws cloudformation delete-stack --stack-name $StackName `
    --region "us-east-1"
