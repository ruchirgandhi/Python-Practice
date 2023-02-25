class Solutions():
    def meetings(self,intervals):
        intervals = sorted(intervals, key=lambda x:x[0])
        for i in range(1,len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False

        return True

s = Solutions()
print(s.meetings([[0,4],[5,10],[15,20]]))











