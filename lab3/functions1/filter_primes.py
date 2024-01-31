def filter_prime(list):
    res = []
    
    for i in list:
        if i == 1:
            continue
        if i == 2:
            res.append(i)
            continue
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            res.append(i)
    return res
    

list = [x for x in map(int, input().split())]

print(filter_prime(list))