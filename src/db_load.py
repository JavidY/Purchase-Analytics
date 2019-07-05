import csv


csv_sources = ['departments.csv']


def read_csv(filename):
    l = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            l.append(row)
    return l

if __name__ == '__main__':
    read_csv(csv_sources[0])
