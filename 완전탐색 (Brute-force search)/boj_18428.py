import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from itertools import combinations

def check(empty_comb):
    for y,x in teachers:
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ty,tx=y,x
            while True:
                ny,nx=ty+dy,tx+dx
                if not 0<=ny<n or not 0<=nx<n:
                    break
                elif (ny,nx) in empty_comb:
                    break
                elif mat[ny][nx]=='S':
                    return False
                ty,tx=ny,nx
    return True
                
                

if __name__=="__main__":
    n=int(input())
    mat=[list(input().split()) for _ in range(n)]
    teachers=[]
    emptys=[]
    for y in range(n):
        for x in range(n):
            if mat[y][x]=='T':
                teachers.append((y,x))
            elif mat[y][x]=='X':
                emptys.append((y,x))
    for empty_comb in combinations(emptys,3):
        if check(empty_comb):
            print("YES")
            exit()
    print("NO")