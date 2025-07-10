import pandas as pd
from dagster import asset, AssetExecutionContext
import boto3
from datetime import datetime

@asset
def load_iris_from_s3(context: AssetExecutionContext) -> pd.DataFrame:
  s3 = boto3.client("s3")
  s3.copy_object(
        Bucket="ukhsa-dev-datalib-ingestion",
        CopySource={
            "Bucket": "ukhsa-dev-datalib-ingestion",
            "Key": "iris.csv"
        },
        Key=f"dagster/iris_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )
