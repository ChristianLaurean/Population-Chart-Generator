import csv


def read_csv(path):
    with open(path, 'r') as data:
        reader = csv.reader(data, delimiter = (','))
        colum = next(reader) 
        data_dict = []
        for row in reader:
            iteratio = zip(colum, row)
            dic_country = {key: value for key, value in iteratio}
            data_dict.append(dic_country)

    return data_dict



            
if __name__ == '__main__':
    read_csv('./data/data.csv')




