from itertools import permutations
from math import sqrt
def make_num(perm):
    ret=0
    for num in perm:
        ret=10*ret+num
    return ret
def is_prime(num):
    if num<=1: return False
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:return False
    return True


def solution(numbers):
    primes=set()
    checked=set()
    nums=list(map(int,numbers))
    for i in range(1,len(numbers)+1):
        for perm in permutations(nums,i):
            new_num=make_num(perm)
            if new_num not in checked:
                checked.add(new_num)
                if is_prime(new_num): primes.add(new_num)
    return len(primes)