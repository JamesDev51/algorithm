import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    times=[list(map(int,input().split())) for _ in range(int(input()))]
    times.sort(key=lambda x:(x[1],x[0]))
    now=-1
    res=0
    for s,e in times:
        if now<=s:
            res+=1
            now=e
    print(res)
    