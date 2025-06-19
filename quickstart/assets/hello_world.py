import pandas as pd

import dagster as dg


@dg.asset
def hello_world():
    return pd.DataFrame({"greeting": ["Hello, World!"]})
