import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

dir_idx=dict()
dir_idx[(-1,0)]=0
dir_idx[(0,1)]=1
dir_idx[(1,0)]=2
dir_idx[(0,-1)]=3

if __name__=="__main__":
    m,n=map(int,input().split())
    mat=[[[0]*4 for _ in range(m+1)] for _ in range(n+1)]
    for _ in range(int(input())):
        b,a,d,c=map(int, input().split())
        dy,dx=c-a,d-b
        mat[a][b][dir_idx[(dy,dx)]]=-1
        mat[c][d][(dir_idx[(dy,dx)]+2)%4]=-1
    dp=[[0]*(m+1) for _ in range(n+1)]
    dp[0][0]=1
    for y in range(n+1):
        for x in range(m+1):
            if y==0 and x==0:continue
            if mat[y][x][0]!=-1 and y-1>=0:
                dp[y][x]+=dp[y-1][x]
            if mat[y][x][3]!=-1 and x-1>=0:
                dp[y][x]+=dp[y][x-1]
    print(dp[-1][-1])
                