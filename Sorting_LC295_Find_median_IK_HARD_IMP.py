

import heapq

class MedianFinder(object):
    def __init__(self):
        ##INITIALIZATION
        self.maxheap = []
        self.minheap = []
        self.median = 0.0

        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)

    def addNum(self,nums):

        if nums <= self.median:
            heapq.heappush(self.maxheap,-nums)
            if len(self.maxheap) - len(self.minheap) == 2:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        else:
            heapq.heappush(self.minheap,nums)
            if len(self.minheap) - len(self.maxheap) == 2:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        self.findMedian()

    def findMedian(self):

        if len(self.maxheap) > len(self.minheap):
            self.median = -self.maxheap[0]
            return self.median

        elif len(self.minheap) > len(self.maxheap):
            self.median = self.minheap[0]
        else:
            self.median = (-self.maxheap[0] + self.minheap[0])//2.0

            return self.median

s= MedianFinder()
s.addNum(5)
s.addNum(5)
s.addNum(5)
print(s.findMedian())



