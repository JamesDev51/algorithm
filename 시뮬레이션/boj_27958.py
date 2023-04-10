import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

from copy import deepcopy
def check():
    score=0
    original_mat=deepcopy(mat)
    cp_mat=deepcopy(mat)
    for i in range(k):
        row=ch[i]
        bullet=bullets[i]
        col=0
        while cp_mat[row][col]==0:
            col+=1
            if col==n:return float('-inf')
        if cp_mat[row][col]<10:#일반 표적
            if bullet<cp_mat[row][col]:cp_mat[row][col]-=bullet
            else:
                cp_mat[row][col]=0 #표적 제거
                score+=original_mat[row][col]
                new_target=original_mat[row][col]//4
                original_mat[row][col]=0 
                if new_target==0:continue
                for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                    ny,nx=row+dy,col+dx
                    if 0<=ny<n and 0<=nx<n and cp_mat[ny][nx]==0:
                        cp_mat[ny][nx]=new_target
                        original_mat[ny][nx]=new_target
        else: #보너스표적
            score+=original_mat[row][col]
            cp_mat[row][col]=0
            original_mat[row][col]=0
    return score

def go(level):
    if level==k:return check()
    ret=0
    for i in range(n):
        ch.append(i)
        ret=max(ret,go(level+1))
        ch.pop()
    return ret
    

if __name__=="__main__":
    n=int(input())
    k=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    bullets=list(map(int,input().split()))
    ch=[]
    print(go(0))