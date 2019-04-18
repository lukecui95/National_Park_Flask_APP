import sqlite3
import unittest
import os.path


class National_parks_Tests(unittest.TestCase):



	def setUp(self):
		self.conn = sqlite3.connect("national_parks.sqlite") # Connecting to database that should exist
		self.cur = self.conn.cursor()

	def test_for_national_park_table(self):
		self.cur.execute("select Name, Type, Location, Challenge_states from Parks where ID = 1")
		data = self.cur.fetchone()
		self.assertEqual(data,('Birmingham Civil Rights', 'National Monument', 'AL', 'AL'), "Testing data that results from selecting Park 1")


	def test_for_states_table(self):
		res = self.cur.execute("select * from States")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the States table')

	def test_states_insert_works(self):
		state = (1,'AL')
		self.cur.execute("insert into States(Id, Name) values (?, ?)", state)
		self.conn.commit()

		self.cur.execute("select Id, Name from countries where Id = 1")
		data = self.cur.fetchone()
		self.assertEqual(data, state, "Testing a select state where Id = 1")

    #Route 1
    def test_for_plot(self):
        res = os.path.exists('static/state_plot.png')
        self.assertTrue(res)

    #Route 2
    def test_num_of_parks(self):
        state = 'AL'
        self.assertEqual(state, 11)

    #Route 3
    def info_of_park(self):
        self.cur.execute("select Type, Location, Challenge_states from Parks where Name = Evergreen")
		data = self.cur.fetchone()
		self.assertEqual(data,('National Park', 'FL', 'FL'), "Testing data that results from selecting Park 1")


    #Route 4
    def test_advice(self):
		pass
        ###Not figure out how to test this route yet.

    def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
