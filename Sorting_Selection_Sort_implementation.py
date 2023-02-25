def selection_sort(array):

    for i in range(len(array)-1):
        index = i

        for j in range(i+1,len(array)):
            if array[j] < array[index]:
                index = j

        if index != i:
            swap(array,index,i)
    return array

def swap(array,i,j):

    temp = array[i]
    array[i] = array[j]
    array[j] = temp

if __name__ == "__main__":
    array = [5,1,10,9,-8,3,8,-7,-6]
    #selection_sort(array)
    print(selection_sort(selection_sort(array)))