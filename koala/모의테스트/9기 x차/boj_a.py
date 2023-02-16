import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n=int(input())
    abilities=list(map(int,input().split()))
    abilities.sort()
    res=float('inf')
    for i in range(n):
        res=min(res,abilities[i]+abilities[-i-1])
    print(res)