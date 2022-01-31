from itertools import permutations
def permutations(string):
    #Implement Your Code Here
    if len(string)==1:
        return [string]
    smalloutput = permutations(string[1:])
    ans=[]
    for i in range(len(smalloutput)):
        for j in range(len(smalloutput[i])+1):
            print(i)
            print(j)

            front = smalloutput[i][:j]
            print(front)

            back = smalloutput[i][j:]
            print(back)


            ans.append(front+string[0]+back)
    return ans
    # permList = permutations(string)
    # for pre in list(permList):
    #     print(' '.join(pre))
    # pass


string = input()
ans = permutations(string)
for s in ans:
    print(s)





