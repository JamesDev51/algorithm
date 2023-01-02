def solution(num, total):
    lt=-1000
    accSum=0
    for initNum in range(lt,lt+num):accSum+=initNum
    rt=initNum
    while rt<=1000:
        if accSum==total:
            return list(range(lt,rt+1))
        accSum-=lt
        lt+=1
        rt+=1
        accSum+=rt
