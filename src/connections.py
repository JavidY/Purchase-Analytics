class Connections:
    def __init__(self, src_conn, tgt_conn):
        self._src_conn = src_conn
        self._tgt_conn = tgt_conn

    @property
    def src_conn(self):
        return self._src_conn

    @property
    def tgt_conn(self):
        return self._tgt_conn


csv_to_oltp = Connections("/input/", "mysql_conn")
