##############
## Define a function named addDigitsInString(...)  which receives a string as a parameter and returns the sum of the digits contained in it. If the string has no digits the function should return the value 0.
## As an example, the following code fragment:
## total  = addDigitsInString("..1..2..3..")
## print (total)
## should produce the output:
## 6
##
#########

def addDigitsInString(st):
    res = 0
    for ch in st:
        if ch.isdigit():
            res += int(ch)
    return res
                
                
total = addDigitsInString("..1..2..3..")
print (total)
