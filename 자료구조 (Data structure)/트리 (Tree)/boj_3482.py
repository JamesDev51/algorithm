import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


def findDot():
    for y in range(r):
        for x in range(c):
            if mat[y][x]==".": return (y,x)
    return (-1,-1)

def bfs(sy,sx):
    ch=[[0]*c for _ in range(r)]
    ch[sy][sx]=1
    que=deque()
    que.append((sy,sx,0))
    ret=[-1,-1,0]
    while que:
        y,x,length=que.popleft()
        if length>=ret[2]:
            ret=[y,x,length]
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<r and 0<=nx<c and not ch[ny][nx] and mat[ny][nx]==".":
                ch[ny][nx]=1
                que.append((ny,nx,length+1))
    return ret
    
            
            

if __name__=="__main__":
    for _ in range(int(input())):
        c,r=map(int,input().split())
        mat=[list(input().strip()) for _ in range(r)]
        sy,sx=findDot()
        res1=bfs(sy,sx)
        res2=bfs(res1[0],res1[1])
        print(f"Maximum rope length is {res2[2]}.")
        
        