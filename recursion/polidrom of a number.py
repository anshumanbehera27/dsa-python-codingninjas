def polidrom(s):
    if len(s) == 0 or len(s) == 1 :
        return True
    else:
        if s[0] != s[-1]:
            return  False
        else:
            return polidrom(s[1:-1])
s = input()
if polidrom(s) == True:
    print("true")
else:
    print(" false")