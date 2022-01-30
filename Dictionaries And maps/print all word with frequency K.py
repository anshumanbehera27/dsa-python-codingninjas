s = "this is a word string having many many word"
k = 2
def printKfre(s,k):
    d = {}
    words = s.split()
    for w in words : # we have to acess all the frequency of the dict
        d[w] =d.get(w,0) +1
    for w in d:
        if d[w] == k:
            print(w)

printKfre(s,k)