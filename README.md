# My National Park Info App - A Flask App (With SQLAlchemy Database)


I built a Flask app using national parks data. My Flask app allows users to get some basic information about the national parks in America by interacting with my app. The first route (a.k.a. home page) will show a graph of the number of national parks in each state. In anther route, data will be displayed via a HTML table to show all the states and the national parks in each state. The third route will allow users to search for a national park they would like to visit and get the basic information about that park. The last route will offer some advice and suggestions to the users. For example, users can type in a kind of national parks they want to visit, then our app will return a list of national parks recommended for our users. Moreover, users can click the "Feeling Adventurous" button in this route. It will also display several "National parks" for our users.

## Repo directory structure

The directory structure for your repo should look like this:
~~~~
├── Database diagram.png
├── Populating_db.py
├── README.md
├── SI507project_tests.py
├── SI507project_tools.py
├── db.py
├── models.py
├── national_parks.csv
├── national_parks.sqlite
├── requirments.txt
├── static
│   └── state_plot.jpeg
└── templates
    ├── _formhelpers.html
    ├── advice.html
    ├── advice_res.html
    ├── index.html
    ├── parks.html
    ├── results.html
    ├── states.html
    └── surprise.html
~~~~

## What did I do?

1. Four main routes.

2. A database contain two tables and one association table(many to many relationship).

3. My choices:
   * Use of a new module "matplotlib".
   * Use of another new module "wtforms".
   * A many-to-many relationship in the database structure that is relied upon during interaction with the Flask application.
   * Two forms in the Flask application that allow a user to interact with the form and show data processed for a user to see.
   * Templating in my Flask application for all routes
   * Links in the views of the Flask application home page that allow a user to navigate the application and view all its routes.
   * Relevant use of built-in libraries itertools: (Route 4: clicking the "Feeling adventurous" button and check it out)
   * Inclusion of JavaScript files in the application that affect the home page in my Flask application.



## National Park Database

### national_parks.csv

This .csv file is used to build our National Parks database.
### models.py

This file is used to design the tables in our database. There are two tables and an association table. The two tables are National_parks and States.

### db.py

This file is used to set and initialize our database.

### Populating_db.py

This file is used to populate our database.

## My Flask Routes

### SI507project_tools.py

I designed all my flask application routes in this file. Those routes can access the National park database and use the data to display messages or enable our users to interact with our app.

### Routes

#### Route 1: http://localhost:5000/

This is the home page and it will show all the routes in our app and a graph about the number of national parks in each state.

#### Route 2: http://localhost:5000/states

This page will show a HTML table containing all the states in America and all the national parks in each state.

#### Route 3:http://localhost:5000/parks

This page will show the basic information of a certain national park. Users can search for a national park they would like to visit and get the basic information about that park.


#### Route 4:http://localhost:5000/advice

This page will provide some advice about national parks for our users. Users can type in what kind of national parks they want to visit, then our app will return a list of national parks recommended for our users. Moreover, users can click the "Feeling Adventurous" button in this route. It will also display several "National parks" for our users.(These National parks are created by using itertools)

#### Additional Routes:

If you take a close look to my codes, you will find there are several additional routes in my flask app. However, those additional routes are not designed for our users to access directly. They are designed to help process data and display messages for route 3 and route 4.

* /results: This route is used in route 3 to show the search results for national parks information.
* /advice_res: This route is used in route 4 to show the search results for advice.
* /adventurous: This route is used to create National parks by using itertools, when our users click the "Feeling Adventurous" button in route 4.

*Note that users should not visit those additional routes by typing in their URLs in the browser.*


## Unit tests - SI507project_tests.py

There are 8 tests in my test suite file.

The first one is used to test my .csv file. Then, I designed four different tests to test my 4 routes. The following tests are used to test my National Park database.

Use command "python SI507project_tests.py" to run me test suite file.

## templates

There are several templates in the templates file. They are used to render HTML which will display in the browser. All the routes use templates to display messages in this app.


## How to run my Flask application


1. cd to the place you saved our files, and then type at the command prompt: python SI507project_tools.py
2. Without doing anything else, in a web a browser, type in and check out this URL: "http://127.0.0.1:5000/".

    It will first display a pop-up window showing the date and time. Click OK and go to our home page. Under the "Navigating my National Parks application" title, you can click different links to access all the routes in our flask application. Moreover, there is a big graph below showing the number of national parks in each state.

3. Change the ULR to "http://localhost:5000/states" or click the "All National Parks" link in the home page.

    You will go to a states page showing all the national parks in each state.

4. Change the ULR to "http://localhost:5000/parks" or click the "Find a national park" link in the home page.

    You will go to the "Find a national park" page, where you can search for the national park you are interested. Type in a national park name and click on the "Search" button. If this national park is in our database, you can see the basic information of this park. Otherwise, our page will display "No results found!".

    You can type in National park names such as Yellowstone, Hot Springs or Everglades, etc.

5. Change the ULR to "http://localhost:5000/advice" or click the "National Parks Advisor" link in the home page.

    You will go to the "National Parks Advisor" page, where users can search a kind of national parks they want to visit. Type in a certain type and click on the "Search" button. If the type of parks are in our database, you can see a list of national parks. Otherwise, our page will display "No results found!".

    You can type in types such as River, Historical, Monument or Preserve, etc.

    Moreover, you can click the "Feeling Adventurous" button. It will also display several "National parks" for our users.(These National parks' names are created by using itertools)



## How to deal with all the files in this project.

*Note that I already created all the files you need to run my flask application, such as the national park database and the graph showed on the home page.*

If you want to go through all the work I did again. Please first delete the "national_parks.sqlite" database.

1. First, cd to the place you saved our files, and then type at the command prompt: python Populating_db.py

    This command enables you to create the database used in our flask routes.

2. Type at the command prompt:python SI507project_tools.py.

    This command is used to run our flask application. See "How to run my Flask application" section.

3. If you want to try my test suite file, type at the command prompt: python SI507project_tests.py

## Use requirements.txt to set your virtual environment

*Note that Since I use matplotlib to create the graph used in route 1, the matplotlib module can cause errors when used in a virtual environment. The official document recommends not to use virtual environment.*

However, if you still want to run my final project in the virtual environment. Please comment the lines below. I already created the graph, so you don't have to create it again.

line 2 :
~~~~
import matplotlib.pyplot as plt
~~~~

line 88 to line 97:

~~~~
def plot_parks():

    df = pd.read_csv('national_parks.csv',encoding='latin-1')
    df_parks_state = df['Web_state'].value_counts().reset_index()
    df_parks_state.columns=['State','Num']

    plt.figure(figsize=(15, 10))
    plt.bar(df_parks_state['State'],df_parks_state['Num'],width=0.35)
    plt.title('The number of National Parks in each state')

    plt.savefig('./static/state_plot.jpeg')
~~~~

line 202:
~~~~
plot_parks()
~~~~

Then, you can run my project in your virtual environment.

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
