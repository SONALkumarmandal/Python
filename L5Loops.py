#LOOPS
#Loops re used to repeat instructions.

count=1
while count<=5:
    print("hi",count)
    count+=1

#Break and Continue

i=1
while i<=5:
    print(i)
    if(i==3):
       break
    i+=1
print("end of loop")


j=1
while j<=5:
    if(j==3):
        j+=1
        continue
    print(j)
    j+=1
print("end of loop")

#Traversing in List , string , tuples etc.

# List traversal
nums=[1,2,3,4,"mango"]

for val in nums:
    print(val)

#Tuple traversal

tup=[1,2,3,4,5,6]
for num in tup:
    print(num)

#string traversal

str = "jai shree ram"

for char in str:
    print(char)

#note 

st="apna college"

for char in st:
    if(char==' '):
        print("printing done")
        break
    print(char)
# else:
#     print("END") #note : does not print END
print("END") # this will print end 

# range()

#Range function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default),
#and stops befoure a specified number.

# range(start?,stop,step?)

for el in range(5): #range(stop)
    print(el)
print(" ")
for el in range(1,5): #range(start,stop)
    print(el)
print(" ")
for el in range(1,5,2): #range(start,stop,step)
    print(el)

seq = range(10)

for i in seq:
    print(i)

#Pass statement : 

for i in range(5):
    pass #if we dont use pass it will give error

print("some useful work")