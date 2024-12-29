#OOPS IN Python

#To map with real world scenarios we started using objects in code.
#This is called object oriented programming.

#this reduces the redundency and increase the reusability.

#Class & Object in Python

#Class is bluePrint for creating objects.

#creating class

class Student:
    #def __init__()  for constructor
    # name="karan kumar"
    name="anonymus" #class attribute
    def __init__(self):  #default construtors
        pass
    def __init__(self,fullname): #constructor(parameterized constructor) takes an argument self (a self parameter is a 
#  reference to the current instance of the class, and is used to access variables that belongs to the class.)
        self.name=fullname #object attribute  it has higher precedence than class attribute
        print("adding new student in database")
#creating objects(instance)

s1=Student("arjun ") #() is used to call the constructor
print(s1.name)

s2=Student("karan")
print(s2.name)


class Car:
    color="blue"
    brand="mercedes"

car1=Car()
print(car1.color)
print(car1.brand)


#Methods

#these are functions that belong to objects.

# class Student:
#     college_name="ABC College"

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def welcome(self):
#         print("welcome student",self.name)
#     def get_marks(self):
#         return self.marks
    
# s1=Student("karan",97)
# s1.welcome()
# print(s1.get_marks())

#Static methods

#Methods that don't use the self parameter(work at class level)

# class Student:
#     @staticmethod #decorator
#     def college():
#         print("ABC College")

# Decorator allows us to wrap another function in order to
# extend the behaviour of the wrapped function, without
#permanently modifying it

#Abstraction : Hiding the implementation details of a class and only showing the essential features to the users.

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")

car1=Car()
car1.start()


#Encapsulation : Wrapping data and functions into a single unit (object).

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("rs.",amount,"was debited")
        print("total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was created")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(1000,1234)
print(acc1.balance)
print(acc1.account_no)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)

