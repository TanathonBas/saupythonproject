#list
my_list = [10,20,30,True,False,"Sale"]
print(my_list)
print(len(my_list))

#tuple
my_tuple = (10,20,30,True,False,"Sale")
print(my_tuple)
print(len(my_tuple))

#set
my_set = {10,20,30,"Hi",True}
print(my_set)
print(len(my_set))

for data in my_set :
    print(data,end="/")

print("-----------------------------------")

listforset = list(my_set)
print(listforset)
listforset[0] = "DTI"
my_set = set(listforset)
print(my_set)


my_set.clear()
print(len(my_set))

my_set1 = {10,20,30,"Hi"}
my_set2 = {10,"Hello","Hi",True}

my_set1.add(999)
print(my_set1)
my_set1.remove("Hi")
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

#len,min,max
print(min(my_set2))
