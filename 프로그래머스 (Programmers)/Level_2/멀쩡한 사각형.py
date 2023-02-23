from math import gcd
def solution(w,h):
    answer = w*h -(w+h-gcd(w,h))
    return answer