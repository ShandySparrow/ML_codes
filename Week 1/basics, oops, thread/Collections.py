# Tuples
print('tuples', end = "\n")
t1 = tuple([1,2,3])
t2 = ('shandy','surveysparrow')
t3 = tuple(t1 + t2)
t3 = tuple(t3)
print(t3)
print(t3[3:],)
print(end="\n")

# dictionaries
print('dictionaries', end = "\n")
d1 = {1 : {'name' : 'shandy', "age" : 22}, 2 : {'name' : 'akash', "age" : 20}}
print(d1.keys())
print(d1.values())
print(d1)
print(d1[1]['name'])

# list
print('list', end = "\n")
l1 = ['name', 'age']
l2 = ['shandy', 22]
for i in range(len(l1)):
    print("{} : {}".format(l1[i],l2[i]))