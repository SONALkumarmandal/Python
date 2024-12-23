#DICTIONARY IN PYTHON

# Dictionaries are used to store data values in key:value pairs
# They are unordered (no indexing), mutable (changeable) & don't allow duplicate keys

info = {
    "key" : "value",
    "name": "apna college",
    "age" : 35,
    "learning" :"coding",  #Note keys cannot be made tuple or List
    "subjects" : ["python","C"], 
    "topics" : ("dict","set"),
    "is_adult" : True,
    "marks" : 94.4,
    12.99 : 94.4
}
print(type(info))

#Accessing Dictionary 
info["name"]="shraddha" #overwrite
info["age"]=20
print(info)

#Creating empty dictionary

null_dict ={}
null_dict["name"]="haldia institute"
print(null_dict) 

# Nesting
student={
  "name":"sonal kumar",
  "subjects":{
      "maths" : 70,
      "english" : 80,
      "phy" :78,
  }
 }
print(student["subjects"]["maths"])
#Dictionary Methods

info.keys() #returns all keys
print(list(student.keys())) #gives number of keys

info.values() #returns all values
print(list(student.values()))

info.items() #returns all (keys,val) pairs as tuples
# print(student.items())
pairs = list(student.items())
print(pairs[0])

info.get("key") #returns the keys according to value
#Note
#avoid using print(student["name2"]) => here name2 key is not present so it will give error
#  and the code that are written below which are correct will not execute 
print(student.get("name2")) #no error --> wil give None

info.update(student) #insert the specified items to the dictionary
new_dict ={"name" : "neha kumar","age" :16} #here if the same key is already present then it will overwrite it with new value
student.update(new_dict)
print(student)


#SET IN PYTHON

#Set is a collection of unordered items
#Each element in the set must be unique & immutable. int , float, strings ,tuple are immutable
#  so they can be stored in set but List and Dictionary are mutable so they are not stored in set.
nums={1,2,3,4}
collection = {1,2,3,3,"hello", "world"}
print(collection)
print(type(collection)) # we can see the order in which they are printed is diffrent so unordered

collection=set() #empty set ; syntex
print(type(collection))

#Set Methods

#note : Sets ate mutable but its elements are immutable so we can add tuple but not List and dict

#set.add(el) adds an element
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apna college")
collection.add((1,2,3))
#set.remove(el) removes the elem an
collection.remove(1) #gives error if elemnt is not availbale

#set.clear() empties the set
collection.clear()

#set.pop() removes a random value
collection = {"hello","apna college" ,"world" ,"coding","python"}
print(collection.pop())
print(collection.pop())

#set.union(set2) combines both set values & returns new
set1 = {1,2,3}
set2 ={2,3,4}
print(set1.union(set2)) #{1,2,3,4}

# set.intersection(set2)
print(set1.intersection(set2)) #{2,3}