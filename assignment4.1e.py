#CMPT 120 
######################################################
##Define a function first_last_repeated which receives as input parameter a string (orig) with at least one character,  and a positive  integer number (repet). The function should return a new string, which has the first character in the original repeated repet times followed by a space and then followed by the last character in the original string also repeated repet times.
##As an example, the following code fragment:
##print (first_last_repeated("abcd",4))
##should produce the output:
##aaaa dddd
##
#######################################################
def first_last_repeated(orig,repet):
    return (orig[0]*repet) + " " + (orig[-1]*repet)

print first_last_repeated("abcd",4)
