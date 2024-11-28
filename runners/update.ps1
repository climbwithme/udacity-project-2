param(
    [string]$StackName,
    [string]$TemplateFilePath,
    [string]$ParametersFilePath
)

aws cloudformation update-stack --stack-name $StackName `
    --template-body file://$TemplateFilePath `
    --parameters file://$ParametersFilePath `
    --capabilities "CAPABILITY_NAMED_IAM" `
    --region "us-east-1"