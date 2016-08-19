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
    stringRes=""
    if ch not in st:
        return ".."
    else:
        for i in range(0,len(st)):
            currentChar = st[i]
            unit = int(i%10)
            if currentChar == ch:
                stringRes += str(unit)
    return (".." + "..".join(stringRes) + "..")
                
s = "abcdabcdabcdabcd"
c = "a"
print(giveMeUnitPos(s,c))
