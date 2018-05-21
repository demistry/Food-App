import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base #package to use base class from for creating new instance of classes
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
class Restaurant(Base):  #create class, passing in instance of base class for its instantiation
    __tablename__ = 'restaurant'
    name = Column(
        String(80), nullable = False) #nullable is used to enforce use of column
    address = Column(
        String (150))
    id = Column(
        Integer, primary_key = True)
    #code to add restaurant name
class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id =Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)




engine = create_engine(
    'sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
