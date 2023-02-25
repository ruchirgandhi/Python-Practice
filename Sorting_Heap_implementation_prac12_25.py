import heapq


def sorting(nums):

    results = []
    heapq.heapify(nums)

    while len(nums) != 0:
        results.append(heapq.heappop(nums))

    return results


print(sorting([3,2,1]))
