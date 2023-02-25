

def dutch(balls):
    start = 0
    current = 0
    n = len(balls) - 1
    while current <= n:
        if balls[current] == "R":
            balls[current], balls[start] = balls[start], balls[current]
            start = start + 1
        if balls[current] == "G":
            current = current + 1
        if balls[current] == "B":
            balls[current], balls[n] = balls[n], balls[current]
            n = n - 1
        else:
            current = current + 1

    return balls


'''
    i = 0
    n = len(balls)
    red = []
    green = []
    blue = []
    for i in range(n):
        if balls[i] == 'R':
            red.append(balls[i])
            i = i + 1
        elif balls[i] == 'G':
            green.append(balls[i])
            i = i+1
        elif balls[i] == "B":
            blue.append(balls[i])
            i = i+1
        else:
            i = i +1


    balls = red + green + blue
    return balls

'''

print(dutch([2,'G','R']))



