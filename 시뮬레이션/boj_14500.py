import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


tetromino_list=[[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(0,1),(1,0),(1,1)],
        [(0,0),(0,-1),(-1,-1),(-2,-1)],[(0,0),(0,1),(-1,1),(-2,1)],
        [(0,0),(1,0),(1,1),(2,1)],[(0,0),(1,0),(1,-1),(2,-1)],
        [(0,0),(0,-1),(0,1),(1,0)]]

def turn():
    global mat
    new_mat=[[0]*LIMIT for _ in range(LIMIT)]
    for y in range(LIMIT):
        for x in range(LIMIT):
            new_mat[x][-y+LIMIT-1]=mat[y][x]
    mat=new_mat

def go():
    global res
    for i in range(4):
        if i!=0:turn()
        for y in range(LIMIT):
            for x in range(LIMIT):
                for tetromino in tetromino_list:
                    sub_sum=0
                    for dy,dx in tetromino:
                        ny,nx=y+dy,x+dx
                        if not 0<=ny<LIMIT or not 0<=nx<LIMIT:break
                        sub_sum+=mat[ny][nx]
                    res=max(res,sub_sum)
                    if res==finish_condition:return

if __name__=="__main__":
    n,m=map(int,input().split())
    LIMIT=max(n,m)
    mat=[[0]*LIMIT for _ in range(LIMIT)]
    largest=float('-inf')
    for y in range(n):
        row=list(map(int,input().split()))
        for x in range(m):
            mat[y][x]=row[x];largest=max(largest,row[x])
    finish_condition=largest*4
    res=float('-inf')
    go()
    print(res)
