from src import oltp_load
import unittest


class TestDbLoad(unittest.TestCase):

    def test_read_csv(self):
        self.assertEqual(oltp_load.read_csv(
            oltp_load.get_input_filenames('departments.csv')[0]),
            [('1', 'frozen'), ('3', 'bakery')])


if __name__ == '__main__':
    unittest.main()
