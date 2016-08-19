##############
## Define a function inBetween(..) which receives a string with at least one character. The function should return a new string, which contains exactly the same characters as the input string, but additionally it should have a star (*) after each of the characters, including a star after the last character.
## As an example, the following code fragment:
## print (inBetween("12abc3"))
## should produce the output:
## 1*2*a*b*c*3*
##
#########

def inBetween(st):
    res = ""
    for ch in st:
        res += ch + "*"
    return res
                
print (inBetween("12abc3"))
