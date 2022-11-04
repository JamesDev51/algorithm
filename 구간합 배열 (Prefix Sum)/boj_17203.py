import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    p_sum=[0]*(n+1)
    for i in range(1,n):
        p_sum[i]=abs(arr[i]-arr[i-1])+p_sum[i-1]
    for _ in range(q):
        i,j=map(int,input().split())
        if j-1<i: print(0)
        else:print(p_sum[j-1]-p_sum[i-1])