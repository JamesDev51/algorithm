from math import gcd

def solution(n, m):
    answer = [gcd(n,m),n*m/gcd(n,m)]
    return answer