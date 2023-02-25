"""
295. Find Median from Data Stream
Hard

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.


"""

import heapq

class MedianFinder(object):

    def __init__(self):
        self.maxheap = []
        self.minheap = []

        self.median = 0.0

        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, nums):
        if nums <= self.median:
            heapq.heappush(self.maxheap,-nums)
            if len(self.maxheap) - len(self.minheap) ==2:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        else:

            heapq.heappush(self.minheap,nums)

            if len(self.minheap) - len(self.maxheap) ==2:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        self.findMedian()

    def findMedian(self):

        if len(self.maxheap) > len(self.minheap):
            self.median = -self.maxheap[0]
            return self.median

        elif len(self.minheap) > len(self.maxheap):
            self.median = self.minheap[0]
            return self.median

        else:
            self.median = (-self.maxheap[0] + self.minheap[0])//2
            return self.median


s= MedianFinder()
s.addNum(5)
s.addNum(10)
s.addNum(15)
print(s.findMedian())



