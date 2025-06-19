import boto3
from dagster import ConfigurableResource

class S3AssumeRoleResource(ConfigurableResource):
    role_arn: str
    session_name: str = "dagster-session"

    def get_client(self):
        session = boto3.Session()
        sts = session.client("sts")
        # Call the assume_role method of the STSConnection object and pass the role ARN and a role session name.
        response = sts.assume_role(
            RoleArn=self.role_arn,
            RoleSessionName=self.session_name
        )
        assumed_session = boto3.Session(
            aws_access_key_id=response["Credentials"]["AccessKeyId"],
            aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
            aws_session_token=response["Credentials"]["SessionToken"],
        )
        return assumed_session.client("s3")
    
# de_session = S3AssumeRoleResource.get_client()
# s3 = de_session.client('s3')