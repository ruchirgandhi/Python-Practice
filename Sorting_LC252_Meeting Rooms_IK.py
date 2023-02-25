

"""
252. Meeting Rooms


Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

"""

def meeting(intervals):

    intervals = sorted(intervals, key = lambda x:x[0])
    #intervals.sort()
    print(intervals)

    for i in range(1,len(intervals)):
        if intervals[i-1][1] > intervals[i][0]:
            return False

    return True


print(meeting([[19,30],[31,10],[15,18]]))
print(meeting([[7,10],[2,4],[15,20]]))































