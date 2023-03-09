import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def back_tracking(l):
    if l==zeros_size:
        for q in mat:
            print(*q)
        exit(0)
    zy,zx=zeros[l]
    num_used=[0]*10
    for x in range(9):num_used[mat[zy][x]]=1
    for y in range(9):num_used[mat[y][zx]]=1
    for y in range(3*(zy//3), 3*(zy//3)+3):
        for x in range(3*(zx//3), 3*(zx//3)+3):
            num_used[mat[y][x]]=1
    for num in range(1,10):
        if not num_used[num]:
            mat[zy][zx]=num
            back_tracking(l+1)
            mat[zy][zx]=0
        

if __name__=="__main__":
    mat=[list(map(int,input().split())) for _ in range(9)]
    zeros=[]
    for y in range(9):
        for x in range(9):
            if not mat[y][x]:zeros.append((y,x))
    zeros_size=len(zeros)
    back_tracking(0)