from sql2 import df

def create_id_data(data):
    temp_id_data = []
    id_data = None
    for x in data.SellStartDate:
        x = str(x).split(sep = ' ')[0]
        id_data = x.split(sep = '-')[0] + x.split(sep = '-')[1]
        print(id_data)
        temp_id_data.append(id_data)

    data.id_data = temp_id_data
#         id_data = x.spl

# create_id_data(df)
print(df)


