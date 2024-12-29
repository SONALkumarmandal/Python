#FILE I/O IN PYTHON

#python can be used to perform operations on a file (read & write data)

# types of all files  i)text files (.txt,docx,.log) ii)binary files (.mp4, .mov, .png)

# note : in system both are stored in 0 and 1s

#Open, read & close File
# we have to open a file before reading or writing

# f=open("file_name","mode") mode-r(read mode) or w(write mode)

f=open("demo.txt","r") #note : if mode is not given r is default
data=f.read()
print(data)
print(type(data))
f.close()

# 'r : open for reading (defalt)
# 'w': open for writing , truncating(data is deleted) the file first
# 'x': create a new file and open it for writing 
# 'a': open for writing , appending to the end of the file if it exists
# 'b : binary mode
# 't':text mode(default)
# '+': open a disk file for uploading(reading and  writing)

#data = f.read() #reads entire file
#data = f.readline() reads one line at a time


line1=f.readline()
print(line1)

line2=f.readline()
print(line2)

f.close()


#Writing to a file

f=open("dem.txt","w")
f.write("I want to learn javascript")
f.close()

#Note : if we use w or f and the file dosen't exist then it is created automatically
#note r+ overwrite the data from beginning (no truncate)
#note w+ read and overwrite from beginning (truncate)
#note a+ read and append at end (no truncate)

#with syntex

with open("demo.txt","a") as f:
    data=f.read()
    print(data)
#with automatically close the file no need to close it

with open("demo.txt","w") as f:
    f.write("new data")

#Deleting a file

#import os
#os.remove("sample.txt")