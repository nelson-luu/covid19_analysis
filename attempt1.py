# Author: Nelson Luu
# Created: 26/05/2020
# Last Modified: 31/07/2020
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
    current = 0
    confirmed = 0
    for i in range(1, len(dataset)):
        if dataset[i][1] in country_dict:
            if bool(re.match("^[1-2]*[0-9]/[0-3][0-9]/[0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%y')
            elif bool(re.match("^[1-2]*[0-9]/[0-3][0-9]/[0-9][0-9][0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%Y')

            country_dict[dataset[i][1]].append([date_object,
                                                int(dataset[i][5]),
                                                int(dataset[i][6]),
                                                int(dataset[i][7])])
        else:
            if bool(re.match("^[1-2]*[0-9]/[0-3][0-9]/[0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%y')

            elif bool(re.match("^[1-2]*[0-9]/[0-3][0-9]/[0-9][0-9][0-9][0-9]$", dataset[i][4])):
                date_object = datetime.strptime(dataset[i][4], '%m/%d/%Y')

            country_dict[dataset[i][1]] = [[date_object,
                                            int(dataset[i][5]),
                                            int(dataset[i][6]),
                                            int(dataset[i][7])]]
    return country_dict


def plot_country(country_name, country_dict):
    from matplotlib import pyplot as plt
    from matplotlib.dates import DateFormatter, MonthLocator

    # initialise variables
    date_val = []
    confirmed_val = []
    deaths_val = []
    recovered_val = []
    current = -1
    confirmed, deaths, recovered = -1, -1, -1
    accumulated_list = []

    # merge counts of the same date
    for value in country_dict[country_name]:
        if current == value[0]:
            confirmed += value[1]
            deaths += value[2]
            recovered += value[3]
            accumulated_list[-1] = ([value[0], confirmed, deaths, recovered])

        else:
            confirmed = value[1]
            deaths = value[2]
            recovered = value[3]
            accumulated_list.append([value[0], confirmed, deaths, recovered])
        current = value[0]

    # retrieve accumulated values into x and y lists for plotting
    for item in accumulated_list:
        date_val.append(item[0])
        confirmed_val.append(item[1])
        deaths_val.append(item[2])
        recovered_val.append(item[3])
        print(item[0], item[1], item[2], item[3])

    # plot graph
    months = MonthLocator()
    monthsFmt = DateFormatter("%b %y")
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)

    # subplot for confirmed cases
    ax1.set_title("Total Confirmed Cases for " + country_name.capitalize())
    ax1.set_ylabel("Number of Confirmed Cases")
    ax1.plot(date_val, confirmed_val)

    # subplot for confirmed cases
    ax2.set_title("Total Confirmed Cases for " + country_name.capitalize())
    ax2.set_ylabel("Number of Deaths")
    ax2.plot(date_val, deaths_val)

    # subplot for confirmed cases
    ax3.set_title("Total Confirmed Cases for " + country_name.capitalize())
    ax3.set_ylabel("Number of Recovered Cases")
    ax3.plot(date_val, recovered_val)

    # prevent overcrowding of date labels
    for subplot in [ax1, ax2, ax3]:
        subplot.xaxis.set_major_locator(months)
        subplot.xaxis.set_major_formatter(monthsFmt)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    my_data = read_file()
    country_dict = get_country_data(my_data)
    country_name = 'Australia'

    plot_country(country_name, country_dict)