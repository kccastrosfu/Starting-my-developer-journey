##############
## Define a Python function called count_digits(...) which receives as a parameter a string and returns the number of digits in the string.
## As an example, the following code fragment:
## s = "..1...1...1...1..."
## print (count_digits(s))
##
## should produce the output:
## 4
##
#########

def  count_digits(st):
    count = 0
    for i in range(len(st)):
        if st[i].isdigit():
            count += 1
    return count

s = "..1...1...1...1..."
print (count_digits(s))
