## NOT GOOD


arr = [1,2,3,0,1,0,0,0,1,2,3,0]


count = 0
n = len(arr)

for i in range(len(arr)):
    if arr[i] != 0:
        arr[count] = arr[i]
        count += 1
    while count < n:
        arr[count] = 0
        count +=1

print(arr)


## NOT GOOD