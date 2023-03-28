import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy

def go():
    global mat
    day=0
    while True:
        ch=[[0]*n for _ in range(n)]
        cp_mat=deepcopy(mat)
        unions=list()
        
        for yy in range(n):
            for xx in range(n):
                if not ch[yy][xx]:
                    ch[yy][xx]=1
                    union=[(yy,xx)]
                    que=deque()
                    que.append((yy,xx))
                    while que:
                        y,x=que.popleft()
                        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                            ny,nx=y+dy,x+dx
                            if 0<=ny<n and 0<=nx<n and not ch[ny][nx] and l<=abs(mat[y][x]-mat[ny][nx])<=r:
                                ch[ny][nx]=1
                                que.append((ny,nx))
                                union.append((ny,nx))
                    if len(union)>1:
                        unions.append(union)
        if not unions:break
        for union in unions:
            cnt_people=sum(mat[union[i][0]][union[i][1]] for  i in range(len(union)))
            avg_people=cnt_people//len(union)
            for y,x in union:
                cp_mat[y][x]=avg_people
        mat=cp_mat        
        day+=1
    return day      
                        
                        
    
    

if __name__=="__main__":
    n,l,r=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(go())