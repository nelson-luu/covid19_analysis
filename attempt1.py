# Author: Nelson Luu
# Created: 26/05/2020
# Last Modified: 26/05/2020
# Description: Plot cases over time for Australia
# Last Update:

def read_file():
    file_name = 'covid_19_clean_complete.csv'
    file_handler = open(file_name, 'r')
    data = []

    for line in file_handler.readlines():
        f_line = line.strip('\n')
        f_line = f_line.split(',')
        data.append(f_line)

    file_handler.close()
    return data

def get_country_data(dataset):
    country_dict = {}
    country_list = []

    # get country names and store in list
    for i in range(1, len(dataset)):
        if dataset[i][1] not in country_list:
            country_list.append(dataset[i][1])

    # for each country, store its data into dictionary
    # fix dates
    for i in range(len(dataset)):
        if dataset[i][1] in country_list:
            country_dict[dataset[i][1]] = dataset[i][4:8]
    return country_dict


if __name__ == '__main__':
    my_data = read_file()
    country_dict = get_country_data(my_data)
    for key, value in country_dict.items():
        print(key, value)