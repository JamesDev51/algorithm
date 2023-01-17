def solution(n):
    answer = 0
    primes=[0]*(n+1)
    for i in range(2,n+1):
        if not primes[i]:
            for j in range(i+i,n+1,i):
                primes[j]=1
    for i in range(2,n+1):
        if not primes[i]:answer+=1
    
    return answer