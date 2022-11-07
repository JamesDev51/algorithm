import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(r1,c1,r2,c2):
    sum=p_sum[r2][c2]-p_sum[r2][c1-1]-p_sum[r1-1][c2]+p_sum[r1-1][c1-1]
    cnt=(r2-r1+1)*(c2-c1+1)
    return sum//cnt
    
if __name__=="__main__":
    r,c,q=map(int,input().split())
    mat=[list(map(int ,input().split())) for _ in range(r)]
    p_sum=[[0]*(c+1) for _ in range(r+1)]
    for y in range(1,r+1):
        for x in range(1,c+1):
            p_sum[y][x]=p_sum[y-1][x]+p_sum[y][x-1]-p_sum[y-1][x-1]+mat[y-1][x-1]
    
    for _ in range(q):
        r1,c1,r2,c2=map(int, input().split())
        print(solve(r1,c1,r2,c2))
        
    