import csv
import config


class Mappings:
    def __init__(self, src_def, src_conn, tgt_conn, tgt_load_stmt):
        self._src_def = src_def
        self._src_conn = src_conn
        self._tgt_conn = tgt_conn
        self._tgt_load_stmt = tgt_load_stmt

    @property
    def src_def(self):
        return self._src_def

    @property
    def src_conn(self):
        return self._src_conn

    @property
    def tgt_conn(self):
        return self._tgt_conn

    @property
    def tgt_load_stmt(self):
        return self._tgt_load_stmt

    # read from csv file and return list
    def read_csv(self, src_def, src_conn):
        filename = '{0}/{1}'.format(src_conn, src_def)
        with open(filename) as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
        return [tuple(row) for row in csv_reader[1:]]

    def extract(self, src_def, src_conn):
        return self.read_csv(src_def, src_conn)

    def load(self, tgt_conn, tgt_load_stmt, data):
        tgt_conn.execute(tgt_load_stmt, data)


load_oltp_departments = Mappings("departments.csv", config.get_input_folder(), "mysql_db", "insert_into")
