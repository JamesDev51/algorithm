import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    p_sum=[0]*(n+1)
    for i in range(n): p_sum[i+1]=p_sum[i]+arr[i]
    m=int(input())
    for _ in range(m):
        i,j=map(int,input().split())
        print(p_sum[j]-p_sum[i-1])
    