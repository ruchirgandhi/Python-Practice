def solve(arr):
    n = len(arr)

    for i in range(n-1):

        if arr[i] % 2 != 0:
            j = (n - 1) - i
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        i += 1
    

    return arr


print(solve([1,2,3,4,5]))
