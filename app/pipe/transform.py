from typing import List

import pandas as pd


def concat_dataframes(data: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatenates a list of pandas DataFrames into a single DataFrame.

    Args:
        data (List[pd.DataFrame]): A list of pandas DataFrames.

    Returns:
        pd.DataFrame: A single DataFrame containing the data from all input DataFrames.

    Example:
        >>> concat_dataframes([DataFrame1, DataFrame2, DataFrame3])
        DataFrame
    """
    return pd.concat(data, ignore_index=True)
