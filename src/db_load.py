import csv
import config


# get folder path to csv files
inp_path = config.get_input_path()


# csv file names
names = ['departments.csv', 'products.csv']


# list of csv file name with full path
csv_files = ['{0}/{1}'.format(inp_path, f) for f in names]


# read from csv file and return list
def read_csv(filename):
    with open(filename) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        return [tuple(row) for row in csv_reader[1:]]


if __name__ == '__main__':
    print(read_csv(csv_files[0]))
