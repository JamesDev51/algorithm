import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,k=map(int,input().split())
    imp="Impossible"
    res=list(range(1,n+1))
    new_res=list(range(1,n+1))
    if n==k: print(imp)
    else:
        for i in range(n-k):
            new_i=(i+1)%(n-k)
            new_res[new_i]=res[i]
        print(*new_res)