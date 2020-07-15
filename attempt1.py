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
    from datetime import datetime
    import re

    country_dict = {}
    country_list = []

    # get country names and store in list
    for i in range(1, len(dataset)):
        if dataset[i][1] not in country_list:
            country_list.append(dataset[i][1])

    # for each country, store its data into dictionary
    # fix dates
    for i in range(1, len(dataset)):
        if dataset[i][1] in country_dict:
            if bool(re.match("^[1-12]/[0-3][1-9]/[0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%y')

            elif bool(re.match("^[1-12]/[0-3][1-9]/[0-9z][0-9][0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%Y')

            country_dict[dataset[i][1]].append([date_object,
                                                int(dataset[i][5]),
                                                int(dataset[i][6]),
                                                int(dataset[i][7])])
            print(dataset[i][4], i)
        else:
            if bool(re.match("^[1-12]/[0-3][1-9]/[0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%y')

            elif bool(re.match("^[1-12]/[0-1][1-9]/[0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%Y')

            country_dict[dataset[i][1]] = [[date_object,
                                            int(dataset[i][5]),
                                            int(dataset[i][6]),
                                            int(dataset[i][7])]]

    return country_dict


def plot_country(country_name, country_dict):
    from matplotlib import pyplot as plt
    from matplotlib import dates as mdates
    date_val = []
    y_val = []
    total_count = 0
    for item in country_dict[country_name]:
        total_count += item[1]
        date_val.append(item[0])
        y_val.append(total_count)

    plt.plot(date_val, y_val)
    plt.gcf().autofmt_xdate()

    plt.show()


if __name__ == '__main__':
    my_data = read_file()
    country_dict = get_country_data(my_data)
    country_name = 'Lesotho'
    print(country_dict)
    #print(plot_country(country_name, country_dict))