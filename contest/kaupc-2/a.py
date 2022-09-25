import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    res=float('-inf')
    for _ in range(n):
        a,d,g=map(int,input().split())
        score=a*(d+g) if a!=d+g else 2*(a*(d+g))
        res=max(res,score)
    print(res)