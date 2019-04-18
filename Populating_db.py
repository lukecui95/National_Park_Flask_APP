from models import National_parks, States
from db import session, init_db
import pandas as pd
import json

init_db()


states_abbr= ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi',
          'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn',
          'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh',
          'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

df = pd.read_csv('national_parks.csv',encoding='latin-1')
df.drop_duplicates(subset='Name',inplace= True)
df= df.reset_index()

for state in states_abbr:
    new_states = States(Name=state.upper())



    for j in range(len(df)):
        if state.upper() in df['Challenge State'][j]:
            check_park = session.query(National_parks).filter_by(Name=df['Name'][j]).first()
            if check_park:
                check_park.state.append(new_states)



            else:
                new_parks = National_parks(Name = df['Name'][j], Type = df['Type'][j], Location = df['Location'][j],
                Description = df['Description'][j],Challenge_states = df['Challenge State'][j])

                new_parks.state.append(new_states)
            session.add(new_states)
            session.commit()
