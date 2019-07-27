from src import db_load
import unittest


class TestDbLoad(unittest.TestCase):

    def test_read_csv(self):
        self.assertEqual(db_load.read_csv(
            db_load.get_input_filenames('departments_test.csv')[0]),
            [('1', 'frozen'), ('3', 'bakery')])


if __name__ == '__main__':
    unittest.main()
