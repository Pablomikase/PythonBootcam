import pandas

raw_data = pandas.read_csv("squirrel_Data.csv")

grey_color_count = len(raw_data[raw_data["Primary Fur Color"] == "Gray"])
black_color_count = len(raw_data[raw_data["Primary Fur Color"] == "Black"])
cinnamon_color_count = len(raw_data[raw_data["Primary Fur Color"] == "Cinnamon"])

print(cinnamon_color_count)

# Creación del diccionario
data_dic = {
    "Color": ["Gray", "Black", "Red"],
    "Count": [grey_color_count, black_color_count, cinnamon_color_count]
}

my_data_frame = pandas.DataFrame(data_dic)
my_data_frame.to_csv("squirells_count.csv")
