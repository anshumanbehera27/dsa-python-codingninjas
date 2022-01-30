a = {1:2 , 3:4 , "list":[1,23] , "dict": {1:2}}
print(a)
print(a['list']) # this the method of accceing the value pf the dict
print(a.get('list'))
print(a.get("li"))# it will show none because it will not present on the dict
print(a.get('li',34))
print(a.keys()) # we can acess the key8s by this

print(a.values()) # it can acess all the value of the dict
print(a.items()) # it can show all the  things are present on it
for i in a :
    print(i ,a[i])
for i in a.values():
    print(i)
print("list" in a)
