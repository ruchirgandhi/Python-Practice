
#Question #1

def square(x):
    return x**2


def digit_sum(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum


try:
    input = int(raw_input('Please Enter Number more than 4 and less than 26: '))
    if  input >= 5 and input <=25:
        print "square of input is", square(input)
        print "Sum of output is", digit_sum(square(input))
    else:
        raise Exception("Sorry, NOT IN RANGE")

except ValueError:
        raise ValueError('Oops, Not an integer, Please try again:')


## SOLUTION


'''

Please Enter Number more than 4 and less than 26: 5
square of input is 25
Sum of output is 7



Please Enter Number more than 4 and less than 26: 20
square of input is 400
Sum of output is 4


Please Enter Number more than 4 and less than 26: 30
Traceback (most recent call last):
  File "/Users/rucgandh/PycharmProjects/HW3/HW3.py", line 21, in <module>
    raise Exception("Sorry, NOT IN RANGE")
Exception: Sorry, NOT IN RANGE

'''

#Question #2

from collections import OrderedDict

file=open('/Users/rucgandh/Downloads/red-headed-league.txt',"r+")

wordcount={}

unwanted_characters = '.,"-;'

for word in file.read().split():
    word = word.strip(unwanted_characters)
    word = word.lower()
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1


d_sorted_by_value = OrderedDict(sorted(wordcount.items(), key=lambda x: x[1]))

for k,v in reversed(d_sorted_by_value.items()[-5:]):
    print k, v


#Solution #2
'''
the 31
to 20
i 18
of 18
and 14
'''

