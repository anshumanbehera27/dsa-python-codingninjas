def isbalanced(string):
    s = []
    for char in string:
        if char in "(":
            s.append(char)
        elif char in ")":
            if( not s or s[-1] != '('):
                return False
            s.pop()
string = input()        if(not s):
            return True
        return False

ans = isbalanced(string)
print(ans)