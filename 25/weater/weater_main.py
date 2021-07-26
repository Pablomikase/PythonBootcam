# with open("weather_data.csv") as data_file:
#    data_line = data_file.readlines()
#    print(data_line)

#Using csv library
#import csv
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
max_value = data["temp"].max()
print(max_value)

