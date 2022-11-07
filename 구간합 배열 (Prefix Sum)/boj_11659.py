import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,m=map(int, input().split())
    arr=list(map(int,input().split()))
    p_sum=[0]*(n+1)
    for i in range(1,n+1): p_sum[i]=p_sum[i-1]+arr[i-1]
    for _ in range(m):
        i,j=map(int,input().split())
        print(p_sum[j]-p_sum[i-1])