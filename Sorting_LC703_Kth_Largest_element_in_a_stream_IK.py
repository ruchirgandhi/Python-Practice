import heapq

class Solutions(object):

    def __init__(self, k, nums):

        self.array = []
        self.maxsize = k

        heapq.heapify(self.array)

        for element in nums:
            if len(self.array) != self.maxsize:
                heapq.heappush(self.array,element)
            elif len(self.array) == self.maxsize:
                heapq.heappushpop(self.array,element)

    def addNum(self, val):

        if len(self.array) != self.maxsize:
            heapq.heappush(self.array,val)
        elif len(self.array) == self.maxsize:
            heapq.heappushpop(self.array, val)

        return self.array[0]


s = Solutions(3,[4,5,6])
print(s.addNum(7))





