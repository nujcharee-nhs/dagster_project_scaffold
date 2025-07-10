def get_s3_defs():

  from dagster import Definitions, load_assets_from_modules
  from .assets import hello_world, iris
  from .resources.assumed_role import S3AssumeRoleResource
  defs = Definitions(
    assets=load_assets_from_modules([hello_world, iris]),
    #     resources={
    #     "s3": S3AssumeRoleResource(
    #         role_arn="arn:aws:iam::605134447797:role/PlatformEngineer",
    #         session_name="dagster-session"
    #     )
    # },
    )

  return defs

defs = get_s3_defs()
