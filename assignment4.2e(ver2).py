##############
## This function digits_plus() receives as input one digit (that is, an integer number greater or equal than 0 and less or equal than 9). The function should return a string. The string will have , alternating, a digit and a "+" symbol, starting with the digit 0, then a plus, then the digit 1, then a plus, and so on, alternating until reaching the input digit and one plus symbol to end the string.
## As an example, the following code fragment:
## print (digits_plus(3))
## should produce the output:
## 0+1+2+3+
##
#########

def digits_plus(num):
    sum_count = ""
    for i in range (num+1):
        sum_count += str(i) + "+"
    return sum_count

print (digits_plus(3))
