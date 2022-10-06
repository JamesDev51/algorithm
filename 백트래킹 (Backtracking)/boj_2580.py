import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def tester(yy,xx):
    num_hash=[1]*10
    for i in range(9): 
        num_hash[mat[yy][i]]=0
        num_hash[mat[i][xx]]=0
    sy=yy//3; sx=xx//3
    for y in range(sy*3,sy*3+3):
        for x in range(sx*3, sx*3+3):
            num_hash[mat[y][x]]=0
    return num_hash


def dfs(l):
    if l==len(zeros):
            for q in mat:print(*q)
            exit(0)
    y,x=zeros[l]
    num_hash=tester(y, x)
    for num in range(1,10):
        if num_hash[num]:
            mat[y][x]=num
            dfs(l+1)
            mat[y][x]=0
    

def solution():
    for y in range(9):
        for x in range(9):
            if not mat[y][x]: zeros.append((y,x))
    dfs(0)
    
if __name__=="__main__":
    mat=[list(map(int,input().split())) for _ in range(9)]
    zeros=list()
    solution()