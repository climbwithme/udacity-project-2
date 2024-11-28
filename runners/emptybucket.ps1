param(
    [string]$BucketName,
    [string]$Region = "us-east-1"
)

# Remove all object versions
$versions = aws s3api list-object-versions --bucket $BucketName | ConvertFrom-Json
if ($versions.Versions) {
    $versions.Versions | ForEach-Object {
        aws s3api delete-object --bucket $BucketName --key $_.Key --version-id $_.VersionId
    }
}

# Remove all delete markers
if ($versions.DeleteMarkers) {
    $versions.DeleteMarkers | ForEach-Object {
        aws s3api delete-object --bucket $BucketName --key $_.Key --version-id $_.VersionId
    }
}

# Remove remaining objects (if versioning is disabled)
aws s3 rm "s3://$BucketName" --recursive

