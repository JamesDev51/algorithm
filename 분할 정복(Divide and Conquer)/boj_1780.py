import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(u,d,l,r):
    if u+1==d and l+1==r: res[mat[u][l]]+=1
    for 
     
if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    res={-1:0,0:0,1:0}
    solve(0,n,0,n)
    print(res[-1])
    print(res[0])
    print(res[1])