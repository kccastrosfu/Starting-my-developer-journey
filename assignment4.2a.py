##############
## Define a function maxDigs(..) which receives as input one string containing digits, letters or special symbols.The function should return an integer number containing the maximum value of all the digits in the string. If there are no digits, the function should return -1
## As an example, the following code fragment:
## print (maxDigs("a1b9c3!$8"))
## should produce the output:
## 9
#########

def maxDigs(word):
    maxNum = -1
    for i in range(len(word)):
        if word[i].isdigit():
            dig = int(word[i])
            if dig > maxNum:
                maxNum = dig
    return maxNum
                
print (maxDigs("a1b9c3!$8"))
