import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem






engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


myFirstRestaurant = Restaurant(name = "Pizza mama put")
myMenuItem = MenuItem(name = "Mama mia", course="Olosho international market Ijebu",
                      description="The food be like wetin sweet", price = "#110.46",
                      restaurant = myFirstRestaurant)

session.add(myFirstRestaurant)
session.add(myMenuItem)
session.commit()
session.query(Restaurant).all()


