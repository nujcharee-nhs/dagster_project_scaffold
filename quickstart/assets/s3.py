import pandas as pd
import dagster as dg
from quickstart.resources.assumed_role import S3AssumeRoleResource
from datetime import datetime


@dg.asset
def s3_asset_staging(s3: S3AssumeRoleResource):
    # Create sample DataFrame
    df = pd.DataFrame({
        "column1": [1, 2, 3],
        "column2": ["A", "B", "C"]
    })

    # Convert to CSV string
    csv_data = df.to_csv(index=False)

    # Get boto3 client
    s3_client = s3.get_client()

    s3_client.put_object(
        Bucket="ukhsa-dev-datalib-staging",
        Key=f"dagster/dummy_ped.csv",
        Body=csv_data
    )

@dg.asset(non_argument_deps={"s3_asset_staging"})
def s3_asset_to_ingestion(s3: S3AssumeRoleResource):
    s3_client = s3.get_client()
    s3_client.copy_object(
        Bucket="ukhsa-dev-datalib-ingestion",
        CopySource={
            "Bucket": "ukhsa-dev-datalib-staging",
            "Key": "dagster/dummy_ped.csv"
        },
        Key=f"dagster/dummy_ped_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )


# Dagster Definitions
defs = dg.Definitions(
    assets=[s3_asset_staging, s3_asset_to_ingestion],
    resources={
        "s3": S3AssumeRoleResource(
            role_arn="arn:aws:iam::605134447797:role/DataEngineer",
            session_name="dagster-session"
        )
    },
)
