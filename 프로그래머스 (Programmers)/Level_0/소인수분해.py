def get_primes(n):
    primes=[0]*(n+1)
    for i in range(2,n+1):
        if not primes[i]:
            for j in range(i+i,n+1,i):
                primes[j]=1
    return primes

def get_next_prime(now_prime,primes):
    for i in range(now_prime+1,len(primes)+1):
        if not primes[i]:
            return i
    

def solution(n):
    answer = []
    primes=get_primes(n)
    prime=1
    while n>1:
        prime=get_next_prime(prime,primes)
        if n%prime==0:
            answer.append(prime)
            while n%prime==0:
                n//=prime
    return answer