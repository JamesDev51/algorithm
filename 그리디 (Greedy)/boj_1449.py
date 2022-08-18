import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,l=map(int,input().split())
    pos=list(map(int,input().split()))
    pos.sort()
    idx=0; res=0
    while idx<n:
        lt=pos[idx]
        rt=lt+l
        while idx<n and pos[idx]+0.5<=rt:idx+=1
        res+=1
    print(res)