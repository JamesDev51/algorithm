import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        b=list(map(int, input().split()))
        res=[]
        if n==2:
            res.append(b[0]);res.append(b[0]);
        else:
            flag=True
            res.append(b[0])
            for i in range(n-2):
                res.append(min(b[i],b[i+1]))
            res.append(b[-1])
        print(*res)
            