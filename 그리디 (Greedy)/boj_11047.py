import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    global k
    cnt=0; idx=n-1
    while 0<k:
        if k<coins[idx]:idx-=1
        else:cnt+=(k//coins[idx]);k%=coins[idx]
    return cnt

if __name__=="__main__":
    n,k=map(int,input().split())
    coins=list(int(input()) for _ in range(n))
    print(solve())