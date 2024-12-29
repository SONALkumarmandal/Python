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

#del keyword

#Used to delete object properties or object itself.

# class Stud:
#     def __init__(self,name):
#         self.name=name
# s1=Stud("sonal")
# print(s1.name)
# del s1.name
# print(s1.name)

#Private(like) attribute & methods

#Conceptual Implementation in Python

#Private attributes & methods are meant to be used only within the class and are not 
# accessible from outside the class.

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)  #this will give you the acc_pass since it is inside the class

acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.acc_pass) #here we can access acc_no and acc_pass outside the class and these are sensitive these are public

#to private it use (__)  ex : to make acc pass private use( self.__acc_pass=acc_pass)

class Person:
    _name="annonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1=Person()


#Inheritance

#when one class(child/derived) derives the properties & methods of another class(parent/base).

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("prius")

# print(car1.color)

#Types of inheritance
# i)single Inheritance
# ii)Multi-level Inheritance
# iii)Multple Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")
#                                     #this is multi level inheritance
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type

# car1=Fortuner("diesel")
# car1.start()


#Multiple Inheritance : derived class can inherit multiple classes properties

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1= C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super method :it is used to access methods of the parent class.

class Car:
    def __init(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")
                                   
class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()

car1=ToyotaCar("prius","electric")
print(car1.type)


#Class Methods :A class method is bound to the class & receives the class as an implicit first argument.
#Note - static method can't access or modify class state & generally for utility.

class Person:
    name="anonymous"

    def changeName(self,name):
        self.name=name  #note : this will not change the value of class attribute upper name
        # but will create another name variable for object attribute which will store "rahul kumar" and the upper name will still have the value "anonomous"
        #to change the class attribute name we can use class Name instead of self 
        # Person.name=name  => now the class attribute value is rahul kumar
        #another method : use self.__class__.name=name
        # using classmethod
        @classmethod
        def changeName(cls,name):
            cls.name=name
p1=Person()
p1.changeNmame("rahul kumar")
print(p1.name)
print(Person.name)

#3 types of methods i)Static Methods  ii)class Methods (cls) iii)Instance method(self)
# when we dont want to change the class attributes we use static methods where to change class attribute we use class Methods when we want to use instance attribute we use instance method


#Property Decorator

#We use @property decorator on any method in the class to use the method as a property.


class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    #Note : On changing any attributes value the percentage will not change it will be fixed so to avoid this issue we use property decorator
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy=86
print(stu1.percentage)

#Polymorphism : Operator Overloading

#When the same operator is allowed to have different meaning according to the contex.

print(1+2) #3
print("apna"+"college") #concatinate 
print([1,2,3]+[4,5,6]) # merge

#here + is an operator and it is used in different forms so here operator overloading takes place
#So when we create class we can use operator overlaoding as well .
#Dunder functions : these functions will give different meaning to the same operator to perform different actions

#Adding two complex numbers

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.real=img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2): #here __add__ is dunder function (__operationToPerform__) 
        newReal=self.real + num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal=self.real - num2.real
        newImg=self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

num3=num1+num2
num3.showNumber()