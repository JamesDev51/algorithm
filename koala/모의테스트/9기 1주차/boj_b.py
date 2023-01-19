import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
    
def solve(start,end,size):
    if dp[start][end]!=float('inf'):return dp[start][end]
    
    for middle in range(size-1):
        now_op_count=matrix[start][0]*matrix[start+middle][1]*matrix[end][1]
        op_count=now_op_count+solve(start,start+middle,1+middle)+solve(start+middle+1,end,size-middle-1)
        dp[start][end]=min(dp[start][end],op_count)
    return dp[start][end]
        
    
if __name__=="__main__":
    n=int(input())
    matrix=[list(map(int, input().split())) for _ in range(n)]
    dp=[[float('inf')]*n for _ in range(n)]
    for i in range(n):dp[i][i]=0
    print(solve(0,n-1,n))
    
    