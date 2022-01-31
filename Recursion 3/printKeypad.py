def getstring(n):
    if n == 2 :
        return "abc"
    if n == 3:
        return "def"
    if n == 4 :
        return "ghi"
    if n == 5:
        return "jkl"
    if n == 6 :
        return "mno"
    if n == 7:
        return "pqrs"
    if n == 8 :
        return "tuv"
    if n == 9 :
        return "wxyz"
    else:
        return " "
def printKeypad(n , outputsofar):
    if n == 0 :
        print(outputsofar)
        return
    smallNumber = n //10
    lastdigit = n % 10
    optionforlastDigit = getstring(lastdigit)
    for c in optionforlastDigit:
        newOutput = c + outputsofar
        printKeypad(smallNumber,newOutput)

printKeypad(23, "")