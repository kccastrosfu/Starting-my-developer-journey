#CMPT 120 
######################################################
##Define a function called repeat_middle which receives as parameter one string (with at least one character), and it should return a new string which will have the middle character/s in the string repeated as many times as the length of the input (original) string.
##
##Notice that if the original string has an odd number of characters there is only one middle character. If, on the other hand, if the original string has an even number of characters then there will be two middle characters, and both have to be repeated (see the example).
##Additionally, if there is only one middle character, then the string should be surrounded by 1 exclamation sign in each extreme . If , on the other hand, the original string has two middle characters then the  returned string should have two exclamation signs at each extreme.
#
##As an example, the following code fragment:
#
##print (repeat_middle("abMNcd"))
#
##should produce the output:
##!!MNMNMNMNMNMN!!

#######################################################
word=("github")
def repeat_middle_odd(word):
    length = len(word)
    middle = int(length/2)
    middle_char = word[middle]
    oddnew_word = middle_char * length
    return "!" + oddnew_word + "!"

def repeat_middle_even(word) :
    length = len(word)
    middle = int(length/2)
    middle_chars = word[middle-1] + word[middle]
    evennew_word = middle_chars * length
    return "!!" + evennew_word + "!!"

def repeat_middle(word):
    length = len(word)
    if length%2==0:
        return repeat_middle_even(word)
    else:
        return repeat_middle_odd(word)
        
print (repeat_middle("abMNcd"))
