#LISTS

#A built-in data type that store set of values
#it can store elements of different types(integer,float,string,etc)

marks1=94.4
marks2=87.3
marks3=90.1 #and so on here a lot of veriable is being created to get rid of this we create list

marks=[94.4,79.1,97.0,76.2]
print(marks)

#Accessing Lists
print(marks[0])
print(marks[1])

#Stroring different data types

student=["karan",95.4,17,"delhi"]
print(student)

#String vs List (in PYTHON)

#String are immutable(changes not allowed) and Lists are mutable(changes allowed)

str="hello"
print(str[0])
# str[0]="y"  (not allowed)

student[0]="arjun"

#Accessing non existing index gives errors

# print(student[10]) gives error

#LIST SLICING (similer to string slicing)

#list_name=[starting_idx : ending_idx] (ending idx is not included)

marks = [85,94,76,63,48]
print(marks[0:2])
print(marks[ :4])
print(marks[1: ])
print(marks[-3:-1])

# LIST METHODS (mutates the original List)

List = [2,1,3]
List.append(4) #adds one element at the end [2,1,3,4]
List.sort() #sorts in ascending order [1,2,3]
#note : on printing it will give None 
print(List.sort())
#sort function will not return anything it is making changes in thr original string (void function)
#sorting apply on strings as well
print(List)
List.sort(reverse=True) #sorts in descending order [3,2,1]
List.reverse() #reverse list
List.insert(0,9) #insert element at index (index,val)
List.remove(1) #removes the first occurence of element
List.pop(1) #removes element at index

# TUPLES

#A built-in data types that lets us create immutable sequence of values.
tup =(87,64,33,95,76)
print(tup[0])
print(tup[1])
# tup[0]=5 (not allowed)

tupp=(1) 
# print(type(tupp)) it will give int
tupp=(1,) #now it will give tuple (compulsory for single element and optional for last) tupp = (1,2,3) or tupp =(1,2,3,)

#TUPLE SLICING => SAME AS LIST

#TUPLE METHODS

tuppl=(2,1,3,1)
# tuppl.index(el) returns index of first occurence tup.index(1) is 1
# tup.count(el) counts total occurences tup.count(1) is 2
