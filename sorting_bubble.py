def bubble_sort(list):
    for i in range(len(list)-1,1,-1):] # range(start, stop, step) here -1 means we have to reverse, list of 4 elements, we need to go to 3,2,1
        for j in range(i): # for each pass (out of 3,2,1 respectively, we need to compare and swap elements)
            if list[j] > list[j+1]:
                temp = list[j]  # this is one the ways of swapping a =5, b =6, temp = a, a = b, b = temp, so a becomes 6 and b becomes 5
                list[j] = list[j+1]
                list[j+1] = temp
    return list



print(bubble_sort([5,7,8,92,4,2,67]))