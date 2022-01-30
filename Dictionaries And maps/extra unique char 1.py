def uniqueChar(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    st=''
    for i in s:
        if i in st:
            continue
        else:
            st+=i
    return st




# Main
s=input()
print(uniqueChar(s))