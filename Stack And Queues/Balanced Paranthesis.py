from sys import stdin


def isBalanced(expression):
    # Your code goes here

    s = []
    for char in expression:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if (not s or s[-1] != '('):
                return False
            s.pop()
        elif char is '}':
            if (not s or s[-1] != '{'):
                return False
            s.pop()
        elif char is ']':
            if (not s or s[-1] != '['):
                return False
            s.pop()
    if (not s):
        return True
    return False


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")

# def isbalanced(string):
#     s = []
#     for char in string:
#         if char in "(":
#             s.append(char)
#         elif char in ")":
#             if( not s or s[-1] != '('):
#                 return False
#             s.pop()
#         if(not s):
#             return True
#     return False
# string = input()
# ans =isbalanced(string)
# if isbalanced(string):
#     print("true")
# else:
#     print("false")
