

def bubble_sort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(length-1-i):  # (here we are doing -1 because we would dont need to go to nth element for next iteration as Nth element is set as max)
            if array[j] > array[j+1]:
                swap(array,j,j+1)

    return array


def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

print(bubble_sort([3,2,-1,-2,1]))