import pandas as pd
import dagster as dg

@dg.asset
def load_iris_from_s3(context: AssetExecutionContext) -> pd.DataFrame:
  s3 = boto3.client("s3")
  s3.copy_object(
        Bucket="ukhsa-dev-datalib-ingestion",
        CopySource={
            "Bucket": "ukhsa-dev-datalib-ingestion",
            "Key": "dagster/iris.csv"
        },
        Key=f"dagster/iris_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )
