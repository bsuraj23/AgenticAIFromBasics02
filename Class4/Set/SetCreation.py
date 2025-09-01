s1 = set()
s2 = {1, 2}
s3 = set([3, 4])
s4 = set(range(5))
s5 = set('hello23')

print(s1, s2, s3, s4, s5)

# temp = (1,2,356,'we',"anup","anup",1,2,356,'we',"anup","anup",1,2,356,'we',"anup","anup")

temp = set(range(5))
print(temp)

# temp = set([3,4])
# temp2= {3,4}
# temp3 =set(range(2))
# # temp23 ={"k",23,True}
# print(temp23)

# methods in set
print(dir(set))  # dir() function gives all the methods available in set        
print(help(set)) # help() function gives the description of all the methods available in set

print(help(set.add)) # help() function gives the description of add method available in set
print(help(set.update)) # help() function gives the description of update method available in set
print(help(set.remove)) # help() function gives the description of remove method available in set   

set.update({5,6,7})
print(set)
set.discard(7)
print(set)