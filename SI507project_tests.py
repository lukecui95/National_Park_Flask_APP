import sqlite3
import unittest
import os.path


class National_parks_csv_test(unittest.TestCase):
	def setUp(self):
		self.parks = open('national_parks.csv','r',encoding="ISO-8859-1")
		self.contents = self.parks.readlines()
		self.parks.close()

	# Testing the required data is successfully stored in my .csv file
	def test_csv_data(self):
		self.assertTrue('National Monument,Birmingham Civil Rights,AL,"\n' in self.contents, "Testing the park data in my .csv file")
		self.assertTrue('National Monument,Cabrillo,"San Diego, CA","\n' in self.contents, "Testing the park data in my .csv file")

class National_parks_database_Tests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("national_parks.sqlite") # Connecting to database that should exist
		self.cur = self.conn.cursor()

	#Route 1: Testing my plot funtion successfully creates the plot.
	def test_for_plot(self):
		res = os.path.exists('static/state_plot.jpeg')
		self.assertTrue(res)

	#Route 2: Testing there are 11 parks in state 1(AL) and our association table works fine.
	def test_num_of_parks(self):
		self.cur.execute("select count(*),States_Id from association where States_Id = 1")
		data = self.cur.fetchone()
		self.assertEqual(data, (11,1))

	#Route 3: Testing the park named Evergreen exists. This route need to search parks based on their names.
	def test_info_of_park(self):
		self.cur.execute("select Type, Location, Challenge_states from Parks where Name = 'Everglades'")
		data = self.cur.fetchone()
		self.assertEqual(data,('National Park', 'Miami, Naples, and Homestead, FL', 'FL'), "Testing data that results from selecting Park 1")

	#Route 4: Testing that we get results from making a fuzzy query.
	def test_advice(self):
		res =self.cur.execute("select * from Parks where Type  LIKE '%River%' ")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that we get results from making a fuzzy query')

    # Testing database table Parks
	def test_for_national_park_table(self):
		self.cur.execute("select Name, Type, Location, Challenge_states from Parks where ID = 1")
		data = self.cur.fetchone()
		self.assertEqual(data,('Birmingham Civil Rights', 'National Monument', 'AL', 'AL'), "Testing data that results from selecting Park 1")

    #Testing database table States
	def test_for_states_table(self):
		res = self.cur.execute("select * from States")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the States table')


    #Testing inserting data works in our database
	def test_states_insert_works(self):
		state = (52,'Test')
		self.cur.execute("insert into States(Id, Name) values (?, ?)", state)
		self.conn.commit()

		self.cur.execute("select Id, Name from States where Id = 52")
		data = self.cur.fetchone()
		self.assertEqual(data, state, "Testing a select state where Id = 52")
		self.cur.execute("DELETE FROM States where Id = 52")

	def tearDown(self):
		self.conn.commit()
		self.conn.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
