# db_load.py
import sys
import unittest
sys.path.insert(0, '../src/')
import db_load  # noqa: E402


class TestDbLoad(unittest.TestCase):

    def test_read_csv(self):
        self.assertEqual(db_load.read_csv(
            "..\\input\\test_data\\departments_test.csv"),
            [('1', 'frozen'), ('3', 'bakery')])


if __name__ == '__main__':
    unittest.main()
