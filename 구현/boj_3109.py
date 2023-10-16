import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
def dfs(y,x):
    if not 0<=y<r or not 0<=x<c:return False
    if mat[y][x]=='x' or ch[y][x]==1:return False
    if x==c-1:return True
    ch[y][x]=1
    return dfs(y-1,x+1) or dfs(y,x+1) or dfs(y+1,x+1)
    

if __name__=="__main__":
    r,c=map(int,input().split())
    mat=[list(input().strip()) for _ in range(r)]
    ch=[[0]*c for _ in range(r)]
    answer=0
    for y in range(r):
        if dfs(y,0):answer+=1
    print(answer)