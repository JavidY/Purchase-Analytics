import csv


csv_sources = ['..\\input\\departments.csv']


def read_csv(filename):
    l = []
    with open(filename) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        return [(row[0], row[1]) for row in csv_reader[1:]]


if __name__ == '__main__':
    print(read_csv(csv_sources[0]))
