import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,x=map(int,input().split())
    c=list(map(int,input().split()))
    c.sort()
    res=0
    not_used=0
    lt,rt=0,n-1
    while lt<=rt:
        if c[rt]==x:
            res+=1
            rt-=1
        elif c[lt]+c[rt]>=x/2:
            res+=1
            lt+=1
            rt-=1
        else:
            not_used+=1
            lt+=1
    print(res+not_used//3)
                