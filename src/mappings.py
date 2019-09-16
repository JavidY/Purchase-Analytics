import csv


class Mappings:
    """A class to defined data flow from source all the way to target."""
    types = {"csv": "csv", "rdbms": "rdbms"}

    def __init__(self, src_query_stmt, src_conn, src_type, tgt_query_stmt, tgt_conn, tgt_load_stmt, tgt_type):
        self._src_query_stmt = src_query_stmt
        self._src_conn = src_conn
        self._src_type = src_type
        self._tgt_query_stmt = tgt_query_stmt
        self._tgt_conn = tgt_conn
        self._tgt_load_stmt = tgt_load_stmt
        self._tgt_type = tgt_type

    # predefined query sql statement. In case type is csv, it is a file name
    @property
    def src_query_stmt(self):
        return self._src_query_stmt

    # connection object, in case of csv it is source folder absolute path
    @property
    def src_conn(self):
        return self._src_conn

    # source type: csv, rdbms. Needed to determine how to read data, from file or rdbms 
    @property
    def src_type(self):
        return self._src_type

    # predefined query sql statement
    @property
    def tgt_query_stmt(self):
        return self._tgt_query_stmt

    # connection object
    @property
    def tgt_conn(self):
        return self._tgt_conn

    # predefined load sql statement
    @property
    def tgt_load_stmt(self):
        return self._tgt_load_stmt

    # target type: csv, rdbms. Needed to determine load type
    @property
    def tgt_type(self):
        return self._tgt_type

    # read data from csv file
    def read_csv(self, file, loc):
        filename = '{0}/{1}'.format(loc, file)
        with open(filename) as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
        return [tuple(row) for row in csv_reader[1:]]

    # read data from rdbms
    def read_db(self, query, conn):
        try:
            conn.cursor.execute(query)
            return conn.cursor.fetchall()
        except Exception as e:
            print("Error while fetching data from db", e)

    # extract data based on query from given system type:csv, rdbms
    def extract(self, query, conn, type):
        if (type == "csv"):
            return self.read_csv(query, conn)
        elif (type == "rdbms"):
            return self.read_db(query, conn)

    # load data into the table
    def load(self, query, conn, values):
        for value in values:
            conn.cursor.execute(query, value)
        conn.commit()

    # identify values exist in source but not in target
    def capture_delta(self, val_1, val_2):
        return set(val_1) - set(val_2)

    # read source , read target, identify delta and load to target
    def etl(self):
        src_values = self.extract(self.src_query_stmt, self.src_conn, self.src_type)
        tgt_values = self.extract(self.tgt_query_stmt, self.tgt_conn, self.tgt_type)
        delta = self.capture_delta(src_values, tgt_values)
        self.load(self.tgt_load_stmt, self.tgt_conn, delta)
