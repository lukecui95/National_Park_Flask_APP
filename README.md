# Final Project - Pengwei Cui


My final project will build a Flask app using data about national parks. My Flask app will allow users to get some basic information about the national parks in America by inputting different data into a URL. The first route (a.k.a. home page) will show a graph of the number of national parks in each state. In anther route, data will be displayed via a HTML table to show all the states in America. A user will be able to select a state they want to visit and see the national parks in this state. The third route will allow users to search for a national park they would like to visit and get the basic information about that park. The last route will offer some advice and suggestions to the users. For example, users can type in the state and what kind of national parks they want to visit, then our app will return a list of national parks recommended for our users.




## National Park Database (Finished)

### national_parks.csv

### models.py

### db.py

### Populating_db.py


## My Flask Routes

### SI507project_tools.py

### Routes

#### Route 1: http://localhost:5000/ . (Finished)

This is the home page and it will show a graph about the number of national parks in each state.

#### Route 2: http://localhost:5000/states (In Progress)

This page will show a HTML table containing all the states in America. A user will be able to click a state they want to visit and see the national parks in this state.

#### Route 3:http://localhost:5000/parks (In Progress)

This page will show the basic information of a certain national park. Users can search for a national park they would like to visit and get the basic information about that park.


#### Route 4:http://localhost:5000/advice

This page will give some advice and suggestions about national parks. Users can type in the form of a state and what kind of national parks they want to visit, then our app will return a list of national parks recommended for our users.


## Unit tests - SI507project_tests.py (In progress)


## How to run my Flask application


## Use requirements.txt to set your virtual environment

1) Create a virtual environment

python3 -m venv finalproject-env

2) Activate your virtual environment

source finalproject-env/bin/activate    # For Mac/Linux...

source finalproject-env/Scripts/activate    # For Windows

3) Install all requirements

pip install -r requirements.txt


4) Try our Flash app

See "How to run our Flash app"

5) Deactivate

deactivate


## National_Parks_database_plan

![Test Image 6](https://github.com/lukecui95/SI507_Final-Project_cpengwei/blob/master/Database%20diagram.png)
