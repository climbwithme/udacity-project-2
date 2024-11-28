# CD12352 - Infrastructure as Code Project Solution
### Project by: Manjunath S C P

## Spin up instructions

### Powershell Scripts Commands:

    .\runners\create.ps1 network-udagram .\network_config\network.yml .\network_config\network-parameters.json
    .\runners\create.ps1 s3-udagram .\s3_config\s3.yml .\s3_config\s3-parameters.json
    .\runners\create.ps1 main-udagram .\udagram_config\udagram.yml .\udagram_config\udagram-parameters.json

### Alternative Python script:

Pre-requisite: 
    
    aws configure

Execution Commands:

    python .\cloud_formation.py create --stack-name network-udagram --template-path ./network_config/network.yml --parameters-path ./network_config/network-parameters.json
    python .\cloud_formation.py create --stack-name s3-udagram --template-path ./s3_config/s3.yml --parameters-path ./s3_config/s3-parameters.json
    python .\cloud_formation.py create --stack-name main-udagram --template-path ./udagram_config/udagram.yml --parameters-path ./udagram_config/udagram-parameters.json

## Tear down instructions
### Powershell Scripts Commands:

    .\runners\delete.ps1 main-udagram
    .\runners\delete.ps1 s3-udagram
    .\runners\delete.ps1 network-udagram

### Alternative Python script:

    python .\cloud_formation.py delete --stack-name main-udagram
    python .\cloud_formation.py delete --stack-name s3-udagram
    python .\cloud_formation.py delete --stack-name network-udagram

## Other considerations
TODO (optional)


## Exercise Details
### 1. Architecture Diagram

![Architecture Diagram](evidences/00_Infrastructure_Diagram.drawio.png)

### 2. CloudFormation Creation

![CloudFormation Creation](evidences/01_CloudFormation_Creation.png)

### 3. Network Resources

![Network Resources](evidences/02_network_resources.png)

### 4. Network Outputs

![Network Outputs](evidences/03_network_outputs.png)

### 5. Udagram Resources

![Udagram Resources](evidences/04_udagram_resources.png)

### 6. Udagram Outputs

![Udagram Outputs](evidences/05_udagram_outputs.png)

### 7. VPC Config - GUI

![Final DNS Snapshot](evidences/a1_key_snaps_vpc_config.png)

### 8. Auto Scaling Config - GUI

![Auto Scaling Config - GUI](evidences/a1_key_snaps_auto_Scaling_config.png)

### 9. Health Checks - GUI

![Health Checks - GUI](evidences/a1_key_snaps_health_check.png)

### 10. Final DNS Snapshot

![Final DNS Snapshot](evidences/06_final_dns_name.png)

### 11. Tear Down

![Tear Down](evidences/07_tear_down_completed.png)

