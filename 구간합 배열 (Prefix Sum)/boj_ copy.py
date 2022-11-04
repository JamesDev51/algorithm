import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,q=map(int,input().split())
    p_sum=[[0]*(n+1) for _ in range(4)]
    for i in range(1,n+1):
        id=int(input())
        p_sum[1][i]+=p_sum[1][i-1]
        p_sum[2][i]+=p_sum[2][i-1]
        p_sum[3][i]+=p_sum[3][i-1]
        p_sum[id][i]+=1
    for _ in range(q):
        a,b=map(int,input().split())
        print((p_sum[1][b]-p_sum[1][a-1]),(p_sum[2][b]-p_sum[2][a-1]),(p_sum[3][b]-p_sum[3][a-1]))