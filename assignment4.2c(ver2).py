##############
## Define a function changeAchar(...)  that receives three parameters: a string (orig) and two characters (ch1 and ch2). The function should return a new string containing the same characters as in the original string (orig) except that in those positions where the character ch1 is in the original string the new string should have the character ch2. If the character ch1 is not present in the original string then the  new string should be the same as the original string.  If characters ch1 is a letter you shoudl only look in the original string  for the exact case (i.e. lower case or upper case)
## As an example, the following code fragment:
## print (changeAChar("---1--1-1--","1","2"))
## should produce the output:
## ---2--2-2--
##
#########

def changeAChar(orig,ch1,ch2):
    if ch1 in orig:
        return orig.replace(ch1,ch2)
    else:
        return orig
                
                
print (changeAChar("---1--1-1--","1","2"))
