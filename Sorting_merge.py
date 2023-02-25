


def merge_sort(array):
    if len(array) > 1:

        mid = len(array)//2

        rightarray = array[mid:]
        leftarray = array[:mid]

        merge_sort(leftarray)
        merge_sort(rightarray)


        i = 0
        j =0
        k =0 #this is for new array/list which we are trying to create

        while i < len(rightarray) and j > len(rightarray):


            if leftarray[i] < rightarray[j]:
                array[k] = leftarray[i]

                i +=1


            else:
                array[k] = rightarray[j]

                j +=1

            k +=1
        while i < len(leftarray):
            array[k] = leftarray[i]

            i += 1
            k += 1

        while j < len(rightarray):
            array[k]= rightarray[j]

            j += 1
            k += 1
        return array

print(merge_sort([10,9,8,1,2,5]))



