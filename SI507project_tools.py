import pandas as pd
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template, session, redirect, url_for,request,flash# tools that will make it easier to build on things
from flask_table import Table, Col
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
from wtforms import Form, StringField, SelectField
from itertools import permutations
import random

# Application configurations


app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'qwertasdfghzxcvbnm'



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./national_parks.sqlite' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

states_abbr= ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi',
          'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn',
          'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh',
          'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']


association_table = db.Table('association',
    db.Column('Parks_ID', db.Integer, db.ForeignKey('Parks.Id')),
    db.Column('States_Id', db.Integer, db.ForeignKey('States.Id'))
    )



#Define table Countries
class National_parks(db.Model):
    __tablename__ = 'Parks' # special variable useful for referencing in other/later code
    # Here we define columns for the table
    # Notice that each column is also basically a class variable
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True) # autoincrements by default
    Name = db.Column(db.Text)
    Type = db.Column(db.Text)
    Location = db.Column(db.Text)
    Description = db.Column(db.Text)

    Challenge_states = db.Column(db.Text)
    Web_state = db.Column(db.String(2))

    #states = relationship("Association", back_populates="park")

    state = db.relationship("States",secondary=association_table,backref="parents")



#Define table ChocolateBars
class States(db.Model):
    __tablename__ = 'States'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.Text)

#Search form used in Route 3
class ParkSearchForm(Form):
    choices = [('Name', 'Name')]
    select = SelectField('Search for a national park:(e.g. Yellowstone, Hot Springs or Everglades, etc)', choices=choices)
    search = StringField('')


#Search form used in Route 4
class AdviceForm(Form):
    choices = [('Type','Type')]
    select = SelectField('Search for a type of National parks:(e.g. River, Historical, Monument or Preserve, etc)', choices=choices)
    search = StringField('')

#Use in route 4
df = pd.read_csv('national_parks.csv',encoding='latin-1')
df.drop_duplicates(subset='Name',inplace= True)
df = df.reset_index()
space = " "

def plot_parks():
    df = pd.read_csv('national_parks.csv',encoding='latin-1')
    df_parks_state = df['Web_state'].value_counts().reset_index()
    df_parks_state.columns=['State','Num']

    plt.figure(figsize=(15, 10))
    plt.bar(df_parks_state['State'],df_parks_state['Num'],width=0.35)
    plt.title('The number of National Parks in each state')

    plt.savefig('./static/state_plot.jpeg')



# Routes
@app.route('/')
def home_page():
    return render_template('index.html')



@app.route('/states')
def show_states():
    all_states = []
    parks = []
    for state in states_abbr:
        parks_name = National_parks.query.filter_by(Web_state=state.upper()).all()
        for park in parks_name:
            parks.append(park.Name)
        all_states.append((state.upper(),parks))
        parks = []

    items = []
    for item in all_states:
        parks_names="   ,   ".join(item[1])
        items.append((item[0],parks_names))

    return render_template('states.html',parks=items)



@app.route('/parks', methods=['GET', 'POST'])
def show_parks():
    search = ParkSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('parks.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    park = []
    name = search.data['search']
    if name != '':
        park = National_parks.query.filter_by(Name=name).all()

    if not park:
        flash('No results found!')
        return redirect('/parks')
    else:
        for p in park:
            results.append((p.Name,p.Type,p.Location,p.Description))

        return render_template('results.html', results=results)

@app.route('/advice',methods=['GET', 'POST'])
def show_advice():
    search = AdviceForm(request.form)
    if request.method == 'POST':
        return adv_results(search)


    return render_template('advice.html', form=search)

@app.route('/advice_res')
def adv_results(search):
    results = []
    park =[]
    type = search.data['search']
    if type != '':
        park = National_parks.query.filter(National_parks.Type.like("%{}%".format(type))).all()

    if not park:
        flash('No results found!')
        return redirect('/advice')
    else:
        for p in park:
            results.append((p.Name,p.Type,p.Location))

        return render_template('advice_res.html', results=results)


@app.route('/adventurous')
def show_surprise():

    all_names=[]
    for i in range(len(df['Name'])):
        all_names.extend(df['Name'][i].split())

    res = list(permutations(all_names,2))

    surprise_parks = []
    count = 0
    while (count<10):
        tmp = random.sample(res,1)
        surprise_parks.append(space.join(tmp[0]))
        count = count +1

    return render_template('surprise.html', parks=surprise_parks )



if __name__ == "__main__":
    db.create_all()
    plot_parks()
    app.run() # run with this: python main_app.py runserver
