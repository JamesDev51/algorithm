import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def spring():
    for y in range(n):
        for x in range(n):
            new_tree=deque()
            while trees[y][x]:
                age=trees[y][x].popleft()
                if nut[y][x]>=age:
                    nut[y][x]-=age
                    new_tree.append(age+1)
                else:
                    dead_trees.append((y,x,age))
            trees[y][x]=new_tree

def summer():
    while dead_trees:
        y,x,age=dead_trees.popleft()
        nut[y][x]+=(age//2)

def fall():
    for y in range(n):
        for x in range(n):
            for age in trees[y][x]:
                if age%5==0:
                    for dy,dx in zip([-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<n and 0<=nx<n:
                            trees[ny][nx].appendleft(1)
                        
def winter():
    for y in range(n):
        for x in range(n):
            nut[y][x]+=feed[y][x]
            
if __name__=="__main__":
    n,m,k=map(int,input().split())
    feed=[list(map(int,input().split())) for _ in range(n)]
    trees=[[deque() for _ in range(n)] for _ in range(n)]
    dead_trees=deque()
    nut=[[5]*n for _ in range(n)]
    for _ in range(m):
        r,c,age=map(int,input().split())
        trees[r-1][c-1].append(age)
    for _ in range(k):
        spring()
        summer()
        fall()
        winter()
    
    ans=0
    for y in range(n):
        for x in range(n):
            ans+=len(trees[y][x])
    print(ans)