import unittest
import db_init


class TestDbInit(unittest.TestCase):


	def test_db_init_tables(self):
		self.assertEqual(db_init.db_init_tables(), ['departments'])


if __name__ == '__main__':
	unittest.main()