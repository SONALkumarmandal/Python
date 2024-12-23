#Printing something

print("Hello World")

#Analyzing this statement 
    # here print is function 

#Python Character set
    #Letters - A to Z , a to z (means it does not contain letters of bengali aur punjabi only english alphabet)
    #Digits - 0 to 9
    #Specal Symbols -+-*/etc
    #WhiteSpace - Blank Space, tab, carriage return , new line, formfeed
    #Other charracters - Python can process all ASCII and Unicode characters as part of data or literals

print("hello veryone")
print("my name is sonal")

#Printing in a single line

print("hello veryone","my name is sonal")

#printing numbers 

print(23)

#printng numbers operations

print(20+10)

# Note : python does not have multiline comment but You can use triple quotes (''' or """) to create a multiline string. While these are technically not comments (they are string literals), if they are not assigned to a variable or used in any way, they are effectively ignored by the interpreter

"""
This is a multiline string,
but it can be used as a comment
if left unassigned.

"""

# Variables

     #Variables are names given to a memory location in a program

name="Sonal"
age=23 #note it stores the value from right to left (Assignment rule)
price=25.25

#Printing variable value

print(name)
print("my name is ",name)
print("my age is ",age)

age2=age

print(age2)

# Identifiers

# Identifiers in Python are the names used to identify variables,functions, classes, modules, or other objects. 
# They act as unique labels that allow you to reference these entities in your code.
#Identifier vs variable

""" 

Identifiers are names used in Python to identify entities like variables, functions, classes, or modules. They act as labels for these objects. For example, my_function is an identifier for a function, or MyClass is an identifier for a class. Identifiers don’t store any data themselves; they are simply names.

The name x is both an identifier and a variable. Here's why:

As an Identifier:

x is the name used to identify a specific entity in the program.
It serves as the label for the memory location where the value 42 is stored.
As a Variable:

x is specifically being used to hold the value 42, making it a variable.
A variable always associates an identifier with a value or object in memory.
So, in this case, x functions as both an identifier (a name) and a variable (storing a value).

"""

#Rules of identifier

""" Allowed Characters:

Must begin with a letter (a-z, A-Z) or an underscore (_).
Can be followed by letters, digits (0-9), or underscores.
No special characters (like @, $, %) are allowed. 

Case Sensitivity:

Identifiers are case-sensitive, meaning Variable and variable are different.

Keywords:

You cannot use Python reserved keywords as identifiers. For example, if, else, class, and def cannot be used.
python
Copy code

No Spaces:

Identifiers cannot contain spaces. Use underscores (_) for readability in multi-word identifiers.

Special Characters and Rules:

Identifiers can start with an underscore. Identifiers starting with a single underscore (e.g., _variable) or double underscores (__variable) have special meanings in Python (like private variables or built-in special methods).
python
Copy code

"""

#Data Types

# Integers (negative positive and zero)
# String   ("shraddha" "sonal")
name1="sk"
name12='sk'
name3='''sk'''
# Float    (4.20)
# Boolean   (True False) T and F should be capital
# None      where we do not want to store any value
a=None # None should be captial

# Keyword : these are the reserved words in python

""" Control Flow:

if, elif, else: Used for conditional statements.
for, while: Used for loops.
break, continue: Modify loop execution.
return: Ends a function and returns a value.

Logical Operators:

and, or, not: Perform logical operations.

Data and Objects:

True, False, None: Represent boolean values and null.

Exception Handling:

try, except, finally, raise: Used for error handling.

Functions and Variables:

def: Defines a function.
global, nonlocal: Modify variable scope.

Class and Modules:

class: Defines a class.
import, from: Import modules.

Asynchronous Programming:

async, await: Used for asynchronous code. """

# Python is Case sensitive A and a is different 
# Note SQL is not case sensitive 

""" Print sum """

a=2
b=5
sum=a+b
print(sum)

# Operators : An operator is a symbol that performs a certain opertions between operands.
# Arihmetic Operators (+,-,*,/,%,**)
# Relational / Comparision Operators (==,!=,>,<=)
# Assignment Operators (=,+=,-=,*=,/=,%=,**=)
# Logical Operators (not, and,or) 

# arithmetic operators 

a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b) # it always gives value in floating point 
print(a%b) 
print(a**b)

# relational operators

a=50 
b=30

print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a>b) #True
print(a<=b) #False
print(a<b) #False


# Assignment operator

num =10
num = num+10 
print(num)

#logical operators 
a=50
b=30
print(not False) #gives true
print(not (a>b))

val1=True
val2=True
print("AND Operator :",val1 and val2) #when both are true
print("OR operator :",val1 or val2) #when one is true

#Conversion
#  i) Type conversion (happens automatically)
#  ii)Type Casting  (happens manually)

#Type conversion 
a=2 #int type
b=4.25  #float type

sum=a+b #python automatically converts a to float since it can store a large number (converts to superior among them)

#Type Casting
a="2"
b=4.25
# print(a+b)  #will give error we have to manually convert a to float
a=float("2")


print(a+b) #no error now a=float("sonal") not possible

#Taking input 

name = input("enter your name : ")
print("welcome : ",name)

# @ the input taken will always be of string type even if you entera number so we net to typecast it @

val=int(input("enter some values : "))
print(val)


# Practice 
# write a program to imput 2 numbers and print their sum
# write a program to input a square and print its area
# input 2 floating point numbers and print their average
#input 2 numbers and print if a is greater than or eqaul to b or not 


