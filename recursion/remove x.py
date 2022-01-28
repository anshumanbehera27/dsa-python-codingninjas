def removex(string):
    if len(string) == 0 :
        return string
    small = removex(string[1:])
    if string[0] == "x" :
        return small
    else:
        return string[0] + small
string = "abxxb"

print(removex(string))
