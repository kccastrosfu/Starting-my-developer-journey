#CMPT 120 
######################################################
##Define a function called remainder _is_even which receives  two positive integer numbers as parameters: num and div. This function should return a boolean value. The value to be returned should be True if the remainder of dividing num by div is even and it should return False otherwise.
##As an example, the following code fragment:
##print (remainder_is_even(23,2))
##should produce the output:
##False
#######################################################
def remainder_is_even(a,b):
    result=a%b
    if result==0 or result==2:
        return True
    if result!=0:
        return False
        return result

print remainder_is_even(23,2)
