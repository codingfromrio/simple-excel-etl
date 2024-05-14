from pipe.extract import extract_from_excel

def main():
    dataframe_list = extract_from_excel("data/input")
    print(dataframe_list)

if __name__ == '__main__':
    main()