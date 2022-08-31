import sys
sys.stdin = open("input.text",  "rt")
import sys
import math
input=sys.stdin.readline

def solve():
    return math.comb(n,k)%mod

if __name__=="__main__":
    n,k=map(int,input().split())
    mod=10007
    print(solve())