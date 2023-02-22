from math import factorial
def solution(n, k):
    answer = []
    num_hash=[0]*(n+1)
    idx=n-1
    while k and idx:
        for num in range(1,n+1):
            if num_hash[num]:continue
            fact=factorial(idx)
            if fact<k:k-=fact
            else:
                idx-=1
                num_hash[num]=1
                answer.append(num)
                break

    for num in range(1,n+1):
        if not num_hash[num]:answer.append(num)
        
    return answer