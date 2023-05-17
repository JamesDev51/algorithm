import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

MOD=1000007
if __name__=="__main__":
    n,m,c=map(int,input().split())
    mat=[[0]*(m+1) for _ in range(n+1)]
    dp=[[[[0]*(c+1) for _ in range(c+1)]for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1][0][0]=1
    for i in range(1,c+1):
        y,x=map(int,input().split())
        mat[y][x]=i
        if y==1  and x==1:
            dp[y][x][0][0]=0
            dp[y][x][i][1]=1
        
    for y in range(1,n+1):
        for x in range(1,m+1):
            if y==1 and x==1:continue
            if mat[y][x]==0:
                for large in range(c+1):
                    for cnt in range(large+1):
                        dp[y][x][large][cnt]+=(dp[y-1][x][large][cnt]+dp[y][x-1][large][cnt])%MOD
            else:
                for large in range(mat[y][x]):
                    for cnt in range(1,mat[y][x]+1):
                        dp[y][x][mat[y][x]][cnt]+=(dp[y-1][x][large][cnt-1]+dp[y][x-1][large][cnt-1])%MOD
    for cnt in range(c+1):
        s=0
        for large in range(c+1):
            s+=dp[n][m][large][cnt]
        print(s%MOD,end=" ")
            