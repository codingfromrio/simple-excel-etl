from pipe.extract import extract_from_excel
from pipe.load import write_df_to_excel
from pipe.transform import concat_dataframes


def main():
    data_frame_list = extract_from_excel('data/input')
    drata_frame = concat_dataframes(data_frame_list)
    write_df_to_excel(drata_frame, 'data/output/output.xlsx')


if __name__ == '__main__':
    main()
    print("testing ci workflow")
