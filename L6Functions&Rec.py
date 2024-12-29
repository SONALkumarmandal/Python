#Functions in python

#Blocks of statements that performs a specific task.

# def func_name(param1,param2..) : <-- function defination

#some work
#return val

#func_name(arg1,arg2..) function call

#calculating sum of 2 numbers 

def calc_sum(a,b): #a,b parameter
    sum=a+b
    print(sum)
    return sum

calc_sum(2,6) #2,6 =>argument

def printHello():
    print("hello")

output=printHello()
print(output)   #function is not returning something so it will give None

def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg(1,2,3)


#Function in Python

#   i)Built-in Function
        # print()
print("apna","college") #print function autometically adds gaps between them sep=" "
print("apna",end="$") # sep ="$" prints on the same line "apna$college"
print("college") #end = "\n"
        # len()
        # type()
        # range()
#   ii)User defined Functions

#Defalut params

def cal_prod(a,b=2): #defalut values should be at the last params
    print(a*b)
    return a*b

#Recursion

def show(n):
    if(n==0):
        return  #controlled return
    print(n)
    show(n-1)

show(4)

#Factorial

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
