import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def check():
    ch=[[0]*c for _ in range(r)]
    for row in range(r-1,-1,-1):
        for col in range(c):
            is_floor=False
            if mat[row][col]=='x' and not ch[row][col]:
                cluster=[]
                ch[row][col]=1
                cluster.append((row,col))
                que=deque();que.append((row,col))
                while que:
                    y,x=que.popleft()
                    if y==r-1:is_floor=True
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<r and 0<=nx<c and mat[ny][nx]=='x' and not ch[ny][nx]:
                            ch[ny][nx]=1
                            que.append((ny,nx))
                            cluster.append((ny,nx))
                if not is_floor:return cluster
    return None
        
def gravity(row,col):
    ret_check=check()
    if ret_check!=None:
        down_cluster=sorted(ret_check,key=lambda x:(-x[0],x[1]))
        while True:
            tmp_down_cluster=[]
            for y,x in down_cluster:
                if not (0<=y+1<r) or mat[y+1][x]!='.' and (y+1,x) not in down_cluster:
                    return
            for y,x in down_cluster:
                mat[y][x]='.'
                mat[y+1][x]='x'
                tmp_down_cluster.append((y+1,x))
            down_cluster=tmp_down_cluster
                        
def solve():
    direction=True #True = left, False = right
    for stick in sticks:
        row=r-stick
        if direction:
            col=0
            while col<c and mat[row][col]=='.':col+=1
            direction=False
        else:
            col=c-1
            while 0<=col and mat[row][col]=='.':col-=1
            direction=True
        if 0<=col<c: #미네랄 부순 경우
            mat[row][col]='.'
            gravity(row,col) #클러스터 중력 작용
            
if __name__=="__main__":
    r,c=map(int,input().split())
    mat=[list(input().strip()) for _ in range(r)]
    n=int(input())
    sticks=list(map(int,input().split()))
    solve()
    for q in mat:
        print(''.join(q))