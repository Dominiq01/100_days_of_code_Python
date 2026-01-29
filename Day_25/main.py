import pandas

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

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg = sum(temp_list) / len(temp_list)
# # print(avg)
#
# avg2 = data["temp"].mean()
# # print(avg2)
#
# largest_temp = data["temp"].max()
# # print(largest_temp)

# Get data from columns
# print(data["temp"])
# print(data.temp)

# Get data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# print(round(data[data.day == "Monday"].temp[0] * 9/5 + 32, 2))

# Create dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_central_park_squirrel_data.csv")

colors_column = squirrel_data["Primary Fur Color"]
squirrel_count = colors_column.value_counts()
squirrel_count.to_csv("squirrel_count.csv")