from src.mappings import Mappings
from src.config import get_input_folder
from src.db_credentials import oltp_db_config
from src.db_class import DbClass
from src.sql_queries import depts_load_sql, depts_query_sql
import unittest


class TestMappings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        csv_conn = get_input_folder()
        csv_file = "departments.csv"
        oltp_conn = DbClass(**oltp_db_config)
        self.oltp_dept_mapping = Mappings(csv_file, csv_conn, "csv", depts_query_sql, oltp_conn, depts_load_sql, "rdbms")
        self.oltp_dept_mapping.tgt_conn.cursor.execute(self.oltp_dept_mapping.tgt_load_stmt, ('1', 'frozen'))
        self.oltp_dept_mapping.tgt_conn.cursor.execute(self.oltp_dept_mapping.tgt_load_stmt, ('2', 'bakery'))
        self.oltp_dept_mapping.tgt_conn.connection.commit()

    def tearDown(self):
        self.oltp_dept_mapping.tgt_conn.cursor.execute("TRUNCATE TABLE departments")
        self.oltp_dept_mapping.tgt_conn.cursor.close()
        self.oltp_dept_mapping.tgt_conn.connection.close()

    def test_read_csv(self):
        self.assertEqual(self.oltp_dept_mapping.read_csv(self.oltp_dept_mapping.src_query_stmt, self.oltp_dept_mapping.src_conn), [('1', 'frozen'), ('2', 'bakery')])

    def test_read_db(self):
        self.assertEqual(self.oltp_dept_mapping.read_db(self.oltp_dept_mapping.tgt_query_stmt, self.oltp_dept_mapping.tgt_conn), [('1', 'frozen'), ('2', 'bakery')])

    def test_capture_delta(self):
        # set1 has a new value. Result: new value
        self.assertEqual(self.oltp_dept_mapping.capture_delta([('1', 'frozen'), ('2', 'bakery'), ('3', 'diary')], [('1', 'frozen'), ('2', 'bakery')]), {('3', 'diary')})
        # set1 has 2 new values. Result: 2 new values
        self.assertEqual(self.oltp_dept_mapping.capture_delta([('1', 'frozen'), ('2', 'bakery'), ('3', 'diary'), ('4', 'furniture')], [('1', 'frozen'), ('2', 'bakery')]), {('3', 'diary'), ('4', 'furniture')})
        # identical sets. Result:Nothing
        self.assertEqual(self.oltp_dept_mapping.capture_delta([('1', 'frozen'), ('2', 'bakery')], [('1', 'frozen'), ('2', 'bakery')]), set())
        # set 2 has new value set 1 not. Result: Nothing
        self.assertEqual(self.oltp_dept_mapping.capture_delta([('1', 'frozen'), ('2', 'bakery')], [('1', 'frozen'), ('2', 'bakery'), ('3', 'diary')]), set())
        # set 1 has 2 same new values. Result: only 1 returned
        self.assertEqual(self.oltp_dept_mapping.capture_delta([('1', 'frozen'), ('2', 'bakery'), ('3', 'diary'), ('3', 'diary')], [('1', 'frozen'), ('2', 'bakery')]), {('3', 'diary')})


if __name__ == '__main__':
    unittest.main()
