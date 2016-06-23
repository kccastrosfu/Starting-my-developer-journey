#CMPT 120 
######################################################
##Define a function named tooth which receives one Boolean parameter named sweet and an integer number n. If sweet is True and the number is 5, the function should return the message: “You have a sweet tooth+5!”. The number is the same as the number n in the parameter. If sweet is False (and number is 5 again) the function  should return the message “You do not have a sweet tooth+5!”.
##As an example, the following code fragment:
##print (tooth(True,1))
##should produce the output:
##You have a sweet tooth+1!
#######################################################
def tooth(sweet,n):
    n = str(n)
    if sweet==True:
        return ("You have a sweet tooth+" + n + "!")
    if sweet==False:
        return ("You do not have a sweet tooth+" + n + "!")
    
print tooth(True,1)
