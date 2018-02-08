# # declare a class and give it name User
# class User(object):
#     # the __init__ method is called every time a new object is created
#     def __init__(self, name, email):
#         # set some instance variables. just like any variable we can call these anything
#         self.name = name
#         self.email = email
#         self.logged = False
#     # this is a method we created to help a user login
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
# #now create an instance of the class
# new_user = User("Anna","anna@anna.com")
# print new_user.email

# class User(object):
#     name = "Anna"
# anna = User()
# print "anna's name: ", anna.name
# User.name = "Bob"
# print "anna's name after change:", anna.name
# bob = User()
# print "bob's name:", bob.name
# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False
# user1 = User("Anna Propas", "anna@anna.com")
# print user1.name
# print user1.logged
# print user1.email
class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage



