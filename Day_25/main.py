# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except ValueError:
#             print("Value can't be converted!")
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])