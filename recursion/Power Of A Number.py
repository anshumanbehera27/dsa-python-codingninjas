## Write your code here
def power(x,n):
    if n == 0 :
        return 1
    
    return x**n
    
## To take space separated input for two variables, we use the following syntax (3 lines)
x,n = input().split()
x = int(x)
n= int(n)
print(power(x,n))
