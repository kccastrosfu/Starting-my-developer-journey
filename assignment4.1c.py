#CMPT 120 
######################################################
##Define a function named food which receives two parameters: an integer value representing the time of the day measured in hours from 0 to 24 and a Boolean value indicating whether a person likes sweets (True) or not (False).
##
##
##
##The function should return one single string with a message as follows.
##
##
##
##  If it is earlier than 6, the message should say "no food" (regardless of the person liking sweets or not).
##  If it is between 6 and 10 extremes included, the message should indicate "breakfast", and if the person likes sweets, additionally, after the word breakfast, there should be a comma and then the word "marmalade", otherwise (if the person does not like sweets and it is breakfast time), after the word breakfast there should be a comma and the word "coffee" (with no spaces after the comma).
##  If the time is between 11 and 15 (extremes included), the message should say "lunch", and if the person likes sweets. additionally, after the word "lunch" there will be a comma and then the word "dessert" (no spaces).
##  Similarly, if it is after 15 or before 22 the message will indicate "dinner", and similarly to lunch, if the person likes sweets there will be a comma and then the word "dessert".
##  If it is 22 or later the returned messages should be again "no food".
##  As an example, the following code fragment:
##  print (food(4,False))
##  should produce the output:
##  no food
#######################################################
def food(hours,sweet):
    if (hours < 6) or (22 < hours):
         return "no food"
    if 6 <= hours <= 10:
        if (sweet):
            return "breakfast" + "," + "marmalade"
        else:
            return "breakfast" + "," + "coffee"
    if 11 <= hours <=15:
        if (sweet):
            return "lunch" + "," + "dessert"
        else:
            return "lunch"
    if 15<=hours <=22:
        if (sweet):
            return "dinner" + "," + "dessert"
        else:
            return "dinner"

print food(4,False)
