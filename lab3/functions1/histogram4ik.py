def histogramino(s):
    for i in s:
        print('*'*i, end= '\n')
    
            
    

list = [x for x in map(int, input().split())]

histogramino(list)