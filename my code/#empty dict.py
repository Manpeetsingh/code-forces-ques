#empty dict
my_dict={}

#dictionary with integer keys
my_dict ={1: 'abc', 2: 'xyz'}
print(my_dict)

#dictionary with mixed keys
my_dict={'name' : 'satish', 1: ['abc', 'xyz']}
print(my_dict)

#create empty dictionary usimh dict
my_dict = dict()

my_dict = dict([(1, 'abc'), (2, 'xyz')])
print(my_dict)

my_dict= {'name': 'satish', 'age':27, 'address': 'gunter'}

#get name
print(my_dict['name'])


#another way of accessing key
print(my_dict.get('address'))

#update name 
my_dict['name']  = 'raju'

print(my_dict)

#add new key 
my_dict['degree']  = 'M.tech'

print(my_dict)

#remove a particular item
print(my_dict.popitem())

print(my_dict)

square={2: 4,3: 9,4: 16,5: 25,6: 36}

#del particular key
del square[2]

print(my_dict)

print(square) # name error because dict is deleted

square={2: 4,3: 9,4: 16,5: 25,6: 36}

my_dict= square.copy()
print(my_dict)

#fromkeys [seq[, v]] > reture a new dictionary with keys 
subject= {}.fromkeys (['math','english','hindi'], 0)
print(subject)

subject={2: 4,3: 9,4: 16,5: 25,6: 36}
print(subject.items()) #return a new view of the dictionary 

#get list of all avialable methods and attribute of dictionary
d ={}
print(dir(d))

#dict comprehension is just like lisk dimensiond but 

d={'a': 1,'b': 2,'c':3,'d':4}
for pair in d.items():
    print(pair)

#c
d= {'a': 1, 'b': 2, 'c': 3, 'd':4}
new_dict = {k:v for k, v in d.items() if v > 2}
print(new_dict)

#operations
d= {'a': 1, 'b': 2, 'c': 3, 'd':4,'e':5}
d= {k+'c':v*2 for k, v in d.items() if v > 2}
print(d)

dict={1:1,2:2,3:3,4:4,5:5}
d= {k:v*v for k, v in d.items()if  v > 0}
print(d)