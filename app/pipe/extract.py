import glob # library to list files in a directory
import pandas as pd # library to work with dataframes

from typing import List

def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    """
    Extracts data from Excel files in a given folder.

    Args:
        input_path (str): The path to the folder containing the Excel files.

    Returns:
        List[pd.DataFrame]: A list of pandas DataFrames, each representing the data from an Excel file.

    Example:
        >>> extract_from_excel('/path/to/excel/files')
        [DataFrame1, DataFrame2, DataFrame3]
    """
    # list all files in the folder
    files = glob.glob(input_path + "/*.xlsx")
    # read all files in the folder
    data = [pd.read_excel(file) for file in files]
    return data

if __name__ == '__main__':
    data = extract_from_excel("data/input")
    print(data)