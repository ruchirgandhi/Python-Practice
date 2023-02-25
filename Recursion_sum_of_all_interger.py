

# for example if n= 4321 return 4 + 3 +2 +1



def sum_of_int(n):

    if len(str(n)) ==1:
        return n

    else:
        return n %10 + sum_of_int(n//10)



print(sum_of_int(4321))


