import pandas as pd
import os

def write_df_to_excel(data: pd.DataFrame, output_path: str) -> None:
    """
    Writes a pandas DataFrame to an Excel file.

    Args:
        data (pd.DataFrame): The DataFrame to be written to the Excel file.
        output_path (str): The path to the output Excel file.

    Returns:
        None

    Example:
        >>> write_df_to_excel(DataFrame, '/path/to/output.xlsx')
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_excel(output_path, index=False)