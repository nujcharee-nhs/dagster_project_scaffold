import pandas as pd

import dagster as dg


@dg.asset
def hello_world():
    """A simple asset that returns a DataFrame with a greeting."""
    return pd.DataFrame({"greeting": ["Hello, World!"]})
defs = dg.Definitions(assets=[processed_data])