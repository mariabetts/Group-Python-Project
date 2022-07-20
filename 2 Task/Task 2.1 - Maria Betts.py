# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:30:42 2022

@author: Maria Betts

Task #1 : Create a class "Customer". The class constructor accepts one parameter: customer name ("name"). 
Restrict direct access to variables of "Customer" class, i.e. make the customer name private and
create function using the property to assign and retrieve value for this variable.
Also create a variable "identifier" inside the "Customer" class, this value should be incremented
by one when creating customers. However it is a variable inside a class, it should show how many customers are created.
Keep the "identifier" assigned to each customer at creation, so that it can be used in other class methods.
Create "get_identifier" method inside the class which returns the customer identifier.
Create method "full_info" inside the class which returns text consisting of customer identifier + customer name.
"""

identifier = 0

class Customers:
    
    identifier = 3
    quantity = 0
    i_d = 1
    
    def __init__(self, customersname):
        self.customersname = customersname
        self.id= Customers.i_d
        Customers.i_d += 1
    def get_identifier(self):
        print("{:d}." . format(self.id))
    def full_info(self):
        print("{}.".format(self.customersname))
        print("{}.".format(self.id))
        
    
c1 = Customers("Jonas Jonaitis")
c2 = Customers("Petras Petraitis")
c3 = Customers("Lukas Lukauskas")

print(Customers.identifier)

print(c1.get_identifier())
print(c2.get_identifier())
print(c3.get_identifier())

print(Customers.identifier)

print(c1.full_info())
print(c2.full_info())
print(c3.full_info())
