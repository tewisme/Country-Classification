#lib
import pandas as pd



def main():
    data_path = '..\\data\\country-data.csv'
    data_dict_path = '..\\data\\data-dictionary.csv'
    data = pd.read_csv(data_path)
    data_dict = pd.read_csv(data_dict_path)
    print(data_dict)

if __name__ == '__main__':
    main()
