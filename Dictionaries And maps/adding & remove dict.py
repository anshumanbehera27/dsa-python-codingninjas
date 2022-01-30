a= {1:2 , 3:4 , 'list': [1,23] ,'dict':{1:3}}
# adding the value
a['t'] = (1,2 ,3)
print(a)
a[1] = 10 # upadte data by using this
b = {3:7 , 'the':4,2:100}
a.update(b) # this function will  modify the value which is preset in a and adding the value which is not present

print(a)
a.pop(1) # this is used to remove the ele from the dict 
print(a)