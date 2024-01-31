def filter_primes(list):
    result = []
    checkprime= lambda x : all(x % j != 0 for j in range(2,x)) if x > 1 else False
    for i in list:
        if i == 1:
            continue
        elif checkprime(i) == True:
            result.append(i)
    return result
                
list = [num for num in map(int, input().split())]

print(filter_primes(list))