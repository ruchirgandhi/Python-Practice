"""
1. Autoscale Policy

A risk modeling system uses a scaling computing system that implements
an autoscale policy depending on the current load or
utilization of the computing system.

It starts with a number of computing instances given by instances.
It polls the instances every second to get
the average utilization at that second, and
performs scaling as described below.

Once an action is taken, the system will stop polling for 10 seconds.
During that time, the number of instances does not change.

Average utilization > 60%: Double the number of instances if
the doubled value does not exceed 2 * 10^8. This is an action.
If the number of instances exceeds this limit upon doubling, perform no action.

Average utilization < 25%: Halve the number of
instances if the number of instances is greater than
1 (take the ceiling if the number is not an integer).
This is also an action. If the number of instances is 1, take no action.

25% ≤ Average utilization ≤ 60%: Take no action.

Given the values of the average utilization at each second as an array, determine the number of instances at the end of the time frame.

Example
instances = 2
averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]


At the first second, averageUtil[0] = 25 ≤ 25, so no action is taken.
At the second second, averageUtil[1] = 23 < 25, so halve the
instances to instances = 2 / 2 = 1.
During the next 10 seconds, averageUtil[2]..averageUtil[11],
no polling is done because an action was taken in the last 10 seconds.
At averageUtil[12] = 76, 76 > 60 so the number of instances is doubled.
There are no more readings to consider and 2 is the final answer.

Function Description
Complete the function finalInstances in the editor below.
The function must return an integer that represents the
final number of instances running.

finalInstances has the following parameter(s):

instances:  an integer that represents the original number of instances running
averageUtil int[]:  an array of integers that
represents the average utilization at each second of the time frame


Constraints

1 ≤ instances < 105
1 ≤ n < 105
0 ≤ averageUtil[i] ≤ 100



Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing

1
3
5
10
80

Sample Output

2
Explanation
instances = 1
averageUtil = [5, 10, 80]

At the 1st and 2nd seconds of the time period, no action will be taken. Even though the utilization is less than 25%, the number of instances is 1. During the 3rd second, the number of instances will be doubled to 2. Therefore, the final answer is 2.

Sample Case 1
Python 3

11011121314151617181920212223
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'finalInstances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER instances
#  2. INTEGER_ARRAY averageUtil
#

Line: 10 Col: 1
Test Results
Custom Input
"""


def Autoscale_Policy(poll,instance):
    count=0
    f=0
    for i in poll:
        if f==1 and count<=10:
            count= count +1
            continue
        else:
            count=0
            print("Hi2")
            f=0
            if i>=25 and i<=60:
                print("Hi3")
                continue
            elif i <25:
                if instance>1:
                    instance=(instance)//2
                    print("HELLO")
                    f=1
                elif i>60:
                    instance=(instance)*(instance)
                    print(instance)
                    f=1
                    if instance >(2**10):
                        f=0
                        continue
    return instance

print(Autoscale_Policy([25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80],2))

#25,23,1,2,3,4,5,6,7,8,9,10,76,80]
