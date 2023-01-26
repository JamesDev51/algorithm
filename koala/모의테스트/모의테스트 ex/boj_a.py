import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    h,w,n,m=map(int,input().split())
    answer=0
    for y in range(0,h,n+1):
        for x in range(0,w,m+1):
            answer+=1
    print(answer)