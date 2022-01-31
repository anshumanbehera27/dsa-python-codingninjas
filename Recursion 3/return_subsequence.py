def subs(s):
    if len(s) == 0 :
        output = []
        output.append("")
        return output
    smallerString = s[1:]
    smallerOutput = subs(smallerString)
    output =[]
    for sub in smallerOutput:
        output.append(sub)
    for sub in smallerOutput:
        sub_with_zero_char = s[0] + sub
        output.append(sub_with_zero_char)
    return output
print(subs("abc"))