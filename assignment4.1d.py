#CMPT 120 
######################################################
##Define a function replaceCharAtPos which receives two input parameters,  a string (orig)  and a positive integer number (pos).
##
##If the number is a position within the string, the function should return a new string. The new string should be the original string except that instead of the original character in that position pos, it should have the position number itself (if the position number has more than 1 digit, the character should be replaced by the digit in the units part of the position number, e.g. 2 if the position number is 12).
##
##
##If the number pos is not a valid position within the original string orig, the string returned should be exactly  the same as the original string.
##
##
##For example
##replaceCharAtPos('abcd',2) should return 'ab2d'
##replaceCharAtPos('abcd',10) should return 'abcd'
##replaceCharAtPos('abcdefghijklmn',12) should return 'abcdefghijkl2n'
##
##As an example, the following code fragment:
##print (replaceCharAtPos("abcd",2))
##should produce the output:
##ab2d

#######################################################
def replaceCharAtPos(orig,pos):
    isPosWithinStr = len(orig) > pos
    if isPosWithinStr:
        return orig[:pos]+ str(pos)[-1] +orig[pos+1:]
    else:
        return orig

print replaceCharAtPos("abcd",2)
