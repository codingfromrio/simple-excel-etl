import pandas as pd
from app.pipe.transform import concat_dataframes

def test_concat_dataframes():
    # Arrange
    arrange = [pd.DataFrame({'A': [1, 2], 'B': [3, 4]}),
               pd.DataFrame({'A': [5, 6], 'B': [7, 8]}),
               pd.DataFrame({'A': [9, 10], 'B': [11, 12]})]
    
    expected = pd.DataFrame({'A': [1, 2, 5, 6, 9, 10],
                             'B': [3, 4, 7, 8, 11, 12]})

    # Act
    act = concat_dataframes(arrange)

    # Assert
    pd.testing.assert_frame_equal(act, expected, check_dtype=False)
