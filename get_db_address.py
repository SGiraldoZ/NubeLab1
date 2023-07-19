import boto3
from botocore.config import Config

get_db_address():
    my_config = Config(
        region_name = 'sa-east-1',
        signature_version = 'v4',
        retries = {
            'max_attempts': 10,
            'mode': 'standard'
        }
    )

    client = boto3.client('ec2',config=my_config,
                            aws_access_key_id="AKIA3F66HZIUA5NAWUHF",
                            aws_secret_access_key="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")

    response = client.describe_instances(InstanceIds=["i-08edc699222776982"])

    db_address = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddress']
    return db_address