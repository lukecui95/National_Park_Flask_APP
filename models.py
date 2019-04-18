from sqlalchemy import Column, ForeignKey, Integer, String, Text, REAL, Table
from sqlalchemy.orm import relationship
from db import Base


association_table = Table('association', Base.metadata,
    Column('Parks_ID', Integer, ForeignKey('Parks.Id')),
    Column('States_Id', Integer, ForeignKey('States.Id'))
    )




#Define table Countries
class National_parks(Base):
    __tablename__ = 'Parks' # special variable useful for referencing in other/later code
    # Here we define columns for the table
    # Notice that each column is also basically a class variable
    Id = Column(Integer, primary_key=True, autoincrement=True) # autoincrements by default
    Name = Column(Text)
    Type = Column(Text)
    Location = Column(Text)
    Description = Column(Text)

    Challenge_states = Column(Text)
    Web_state = Column(String(2))

    #states = relationship("Association", back_populates="park")

    state = relationship("States",secondary=association_table,backref="parents")



#Define table ChocolateBars
class States(Base):
    __tablename__ = 'States'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(Text)

    #park = relationship("Parks",secondary=association_table,backref="parents")

    #parks = relationship("Association", back_populates="state")
