"""
Created on Tue May 10 16:30:10 2022

@author: Maria Betts

Task #4 : Print the items of all shops, as well as the components of those items.
"""

from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine("sqlite:///:memory:", echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Shop(Base):
    __tablename__ = "shops"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    address = Column(String(100))
    items = relationship("Item", back_populates="shop")
    
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    barcode = Column(String(32), unique=True)
    name = Column(String(40), nullable=False)
    description = Column(String(200), default='EMPTY')
    unit_price = Column(Numeric(10, 2), nullable=False, default='record creation date and time')
    created_at = Column(DateTime(timezone=True), default=func.now())
    shop_id = Column(Integer, ForeignKey("shops.id"))
    shop = relationship("Shop", back_populates="items")
    components = relationship("Component", back_populates="item")
    
class Component(Base):
    __tablename__ = "components"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    quantity = Column(Numeric(10, 2), default='1.00')
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", back_populates="components")

Base.metadata.create_all(engine)

shop_1 = Shop(name="IKI", address="Kaunas, Iki street 1")
shop_2 = Shop(name="MAXIMA", address="Kaunas, Maksima street 2")

session.add(shop_1)
session.add(shop_2)

session.commit()

item_1 = Item(barcode='112233112233', name='Žemaičių bread', unit_price=1.55, shop_id=shop_1.id)
item_2 = Item(barcode='33333222111', description='Milk from Klaipeda', name='Klaipeda milk', unit_price=2.69, shop_id=shop_1.id)
item_3 = Item(barcode='99898989898', name='Aukštaičių bread', unit_price=1.65, shop_id=shop_2.id)
item_4 = Item(barcode='99919191991', description='Milk from Vilnius', name='Vilnius milk', unit_price=2.99, shop_id=shop_2.id)

session.add(item_1)
session.add(item_2)
session.add(item_3)
session.add(item_4)

session.commit()

component_1 = Component(name='Flour', quantity=1.50, item_id=item_1.id)
component_2 = Component(name='Water', quantity=1.50, item_id=item_1.id)
component_3 = Component(name='Milk', quantity=1.50, item_id=item_2.id)
component_4 = Component(name='Flour', quantity=1.50, item_id=item_3.id)
component_5 = Component(name='Water', quantity=1.50, item_id=item_3.id)
component_6 = Component(name='Milk', quantity=1.50, item_id=item_4.id)

session.add(component_1)
session.add(component_2)
session.add(component_3)
session.add(component_4)
session.add(component_5)
session.add(component_6)

session.commit()

print(shop_1.name, shop_1.address)
print(item_2.name, item_2.description, item_2.unit_price)
print(shop_2.name, item_3.name, component_5.name)

# Task 3
'''
Replace component 'Water' quantity from 1.00 to 1.45 of 'Žemaičių bread', which is in the 'IKI' shop.
Delete component 'Milk' from 'Vilnius milk', which is in the 'MAXIMA' shop. 
'''

temp = component_2.quantity
component_2.quantity = item_1.unit_price
session.commit()

item_1.unit_price = temp

session.delete(component_6)
session.commit()

## Task 4

print(item_1.barcode,item_1.name,item_1.unit_price,item_1.shop_id)
print(item_2.barcode,item_2.description,item_2.name,item_2.unit_price,item_2.shop_id)
print(item_3.barcode,item_3.name,item_3.unit_price,item_3.shop_id)
print(item_4.barcode,item_4.description,item_4.name,item_4.unit_price,item_4.shop_id)

print(component_1.name,component_1.quantity,component_1.item_id)
print(component_2.name,component_2.quantity,component_2.item_id)
print(component_3.name,component_3.quantity,component_3.item_id)
print(component_4.name,component_4.quantity,component_4.item_id)
print(component_5.name,component_5.quantity,component_5.item_id)
print(component_6.name,component_6.quantity,component_6.item_id)