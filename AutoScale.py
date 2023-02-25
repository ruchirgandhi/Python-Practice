def autoScale(instance, Poll):
    #lim_l = 1
    max = 200000000
    #th_l = 25
    #th_h = 60
    wait = 10
    count = 0
    length = len(Poll)
    ans = instance
    while count < length:
        print(f'{count}-th second, utility is {Poll[count]}, instance number before action is {ans}')
        if Poll[count] < 25 and ans > 1:
            ans = (ans + 1) // 2
            count= count + wait
        elif Poll[count] > 60 and ans <= max:
            ans = ans * 2
            count = count + wait
        count += 1
    return ans


instance, Poll = 1, [5, 10, 80]
print(autoScale(instance, Poll))

instance, Poll = 2, [5, 6, 30, 5, 4, 8, 19, 89]
print(autoScale(instance, Poll))