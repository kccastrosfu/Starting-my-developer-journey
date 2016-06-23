#CMPT 120 
######################################################
##This is a test question. Define a function firstIsSmaller(...)  which receives two values as parameters and returns the  Boolean value True is the first value is less than the second value  and returns the value false otherwise. Hint: save the value to be returned in a variable and then return such variable, so that you have a unique return statement in the code.
##As an example, the following code fragment:
##print (firstIsSmaller(1,2))
##should produce the output:
##True

#######################################################
def firstIsSmaller(a,b):
    if a<b:
        return True
    if a>=b:
        return False 
    
print firstIsSmaller(1,2)
