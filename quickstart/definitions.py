def get_s3_defs():

  from dagster import Definitions, load_assets_from_modules
  from .assets import s3 
  from .resources.assumed_role import S3AssumeRoleResource
  defs = Definitions(

        assets=load_assets_from_modules([s3]),
        resources={
        "s3": S3AssumeRoleResource(
            role_arn="arn:aws:iam::605134447797:role/DataEngineer",
            session_name="dagster-session"
        )
    },
    )

  return defs

defs = get_s3_defs()
