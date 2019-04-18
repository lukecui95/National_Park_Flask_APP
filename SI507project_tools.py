import pandas as pd
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this


# Application configurations
app = Flask(__name__)


app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'qwertasdfghzxcvbnm'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./SI507_project3.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy



def plot_parks():
    df = pd.read_csv('national_parks.csv',encoding='latin-1')
    df_parks_state = df['Web_state'].value_counts().reset_index()
    df_parks_state.columns=['State','Num']

    plt.figure(figsize=(15, 10))
    plt.bar(df_parks_state['State'],df_parks_state['Num'],width=0.35)
    plt.title('The number of National Parks in each state')

    plt.savefig('state_plot.png')


# Routes
@app.route('/')
def home_page():
    return render_template('index.html')


# @app.route('/states')
# def show_states():
#
# @app.route('/parks')
# def show_parks():
#
# @app.route('/advice')
# def show_advice():




if __name__ == "__main__":
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    plot_parks()
    app.run() # run with this: python main_app.py runserver
