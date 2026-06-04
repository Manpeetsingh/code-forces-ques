t =(1,2,3,4,5,6)

print(t[1:4])

#print elements from starting to second last elements
print(t[:-2])

#print elements from starting to end 
print(t[:])

#concatinating tuple

t=(1,2,3 )+(4,5,6)
print(t)

t = (('satish', )* 4)
print(t)

#delete entire tuple using del keyboard
t =(1,2,3,4,5,6)

#delete entire tuple
del t

t= (1,2,3,1,3,3,4,1)

print(t.index(3))# return index of the first element

#print index of the code1

#test if the element is true otr false
t =(1,2,3,4,5,6)

print(1 in t)

print(7 in t)

t =(1,2,3,4,5,6)
print(len(t))

t =(1,2,3,4,5,6)
new_t = sorted(t)
print(new_t)# test the num if it exist in tuple or not

# get the largest nom in tuple
t =(1,2,3,4,5,6)

print(max(t))
 
 #print the sum of all no
t =(1,2,3,4,5,6)
print(sum(t))



#2. highest and lowest price


 
price=(120,80,150,200,90)
print(min(price))
print(max(price))

#1. total money
price=(120,80,150,200,90)
print(sum(price))

#3. total item sold more than 100rs
price=(120,80,150,200,90)
print(100<(price))