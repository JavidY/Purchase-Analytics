import csv
import config


names = ('departments.csv', 'products.csv')


# returns full path from the given list of files.
def get_input_filenames(*names):
    folder = config.get_input_folder()
    return ['{0}\\{1}'.format(folder, f) for f in names]


# read from csv file and return list
def read_csv(filename):
    with open(filename) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        return [tuple(row) for row in csv_reader[1:]]


if __name__ == '__main__':
    print(read_csv(get_input_filenames(*names)[0]))
