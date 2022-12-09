import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(num):
    if num==0:return 1
    if num in memo: return memo[num]
    memo[num]=solve(num//p)+solve(num//q)
    return memo[num]

if __name__=="__main__":
    n,p,q=map(int,input().split())
    memo=dict()
    print(solve(n))