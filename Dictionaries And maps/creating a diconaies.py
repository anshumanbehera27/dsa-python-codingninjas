# first way of creating dic
a= {"the":1 , "a":5 , 10000:"abc"}
print(type(a))
print(a)
print(len(a))
# 2nd way of creating
b = a.copy()
print(b)
# 3rd way of creating the dict
c = dict([("the",6),("f",7) ,(2,4)]) # we have to put the key and value in a pair
print(c)
d = dict.fromkeys(["abc", 32  , 4])# we can put the key only thats why it show the  none
print(d)
d = dict.fromkeys(["abc", 32 , 4],10)
print(d)