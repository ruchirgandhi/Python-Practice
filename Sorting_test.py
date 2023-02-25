def dist(x):
    return x[0]**2 + x[1]**2

def test(points,K):
    lst = [(i,dist(i)) for i in points]
    return lst



print(test(([-3,2],[0,3],[1,4],[0,0]),2))


