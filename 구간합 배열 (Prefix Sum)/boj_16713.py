import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    p_sum=[0]*(n+1)
    
    for i in range(1,n+1):
        p_sum[i]=p_sum[i-1]^arr[i-1]
    

    res=0

    for _ in range(q):
        s,e=map(int,input().split())
        res^=(p_sum[e]^p_sum[s-1])
    print(res)