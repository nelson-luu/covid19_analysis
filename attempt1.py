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

def get_country(country_name, dataset):
    country_data = {}
    for i in range(len(dataset)):
        if dataset[i][1] == country_name:
            country_data[country_name] = dataset[i][4:8]



my_data = read_file()
