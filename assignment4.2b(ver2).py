##############
## Define a function giveMeUnitPos(...)  which receives one string (st) and one character (ch) and returns a new string containing the unit part of the positions (i.e. the rightmost digit in the position number) where the character is found, each position digit separated by two dots (and at the start and end of the string to be returned there should also be two dots).   If the character ch  is  the not present in the original string then the function should return a string containing only two dots.
## As an example, the following code fragment:
## s = "abcdabcdabcdabcd"
## c = "a"
## print(giveMeUnitPos(s,c))
## should produce the output:
## ..0..4..8..2..
##
#########

def giveMeUnitPos(st,ch):
    res = ".."
    for i in range(len(st)):
        if (ch == st[i]):
            unit = int(i % 10)
            res += str(unit) + ".."
    return res
                
s = "abcdabcdabcdabcd"
c = "a"
print(giveMeUnitPos(s,c))
