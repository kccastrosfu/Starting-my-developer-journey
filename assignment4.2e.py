##############
## This function digits_plus() receives as input one digit (that is, an integer number greater or equal than 0 and less or equal than 9). The function should return a string. The string will have , alternating, a digit and a "+" symbol, starting with the digit 0, then a plus, then the digit 1, then a plus, and so on, alternating until reaching the input digit and one plus symbol to end the string.
## As an example, the following code fragment:
## print (digits_plus(3))
## should produce the output:
## 0+1+2+3+
##
#########

def digits_plus(num):
    count = 0
    sum_count  = ""
    while (count < num):
        count += 1
        sum_count = sum_count + str(count)
    sum_count = "+".join(str(sum_count))
    if count == 0:
        return ("0+" + sum_count)
    else:
        return ("0+" + sum_count  + "+")

print (digits_plus(3))
