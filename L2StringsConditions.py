#Strings 

str1="This is a \nstring"
str2='student'
str3="""this is a string"""
print(str1)
# 'this is sonal's book'  it will give error 
"this is sonal's book"  #no error
#this is why we need different quote

#STRING OPERATIONS

#concatination "hello" + "world" ="helloworld"
str1="apna"
str2="college"
final_str=str1+str2
print(final_str)

#length of str len(str)
print(len(str1))

#indexing : zero based
print(str1[0])

#Note : we cannot change the value at particular index
# ex- str1[0]="q" =>not possible

#SLICING : Accessing parts of a string  to access str[starting_idx : ending_idx] 
#ending idx is not included
#str[ :4] is same as str[0:4]
#str[1: ] is same as str[1: len(str)]
str="my name"

print(str[5:12])

#using negative Index

str3="Apple" # here from right to left index values -1 to -5
print(str3[-3:-1])


#STRING FUNCTIONS

#str= "i am a coder"
#str.endswith("er") =>returns true if string ends with substr
#str.capitalize() =>capitalize 1st char
str4="i am sonal"
print(str4.capitalize()) #it does not changes the original string str4 only prints the capitalized string
print(str4)
#str.replace(old,new) => replaces all occurences of old with new 
#str.find(word) => returns 1st index of 1st ocurence
print(str4.find("am"))
#str.count("am") => counts the occurences of substr in string

# QUESTIONS
# write a program to input users first name and print its length

name=input("enter your name") 
print(len(name))

#CONDITIONAL STATEMENTS

light=""

if(light=="red"):
    print("stop") #four spaces are required or tab in vs code (indentation)
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("end")

#NESTING

age = 95
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")