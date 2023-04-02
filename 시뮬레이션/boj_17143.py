import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def fish(col):
    for y in range(r):
        if mat[y][col]:
            s,d,z=mat[y][col]
            mat[y][col]=[]
            return z
    return 0
def move():
    global mat
    new_mat=[[[] for _ in range(c)] for _ in range(r)]
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    for yy in range(r):
        for xx in range(c):
            if mat[yy][xx]:
                y,x=yy,xx
                s,d,z=mat[y][x]
                if d in [0,2]:real_s=s%((r-1)*2)
                else:real_s=s%((c-1)*2)
                for _ in range(real_s):
                    ny,nx=y+dy[d],x+dx[d]
                    if not 0<=ny<r or not 0<=nx<c:
                        d=(d+2)%4
                        ny,nx=y+dy[d],x+dx[d]
                    y,x=ny,nx
                if new_mat[y][x]:
                    if new_mat[y][x][2]<z:new_mat[y][x]=[s,d,z]
                else:
                    new_mat[y][x]=[s,d,z]
    mat=new_mat
if __name__=="__main__":
    r,c,m=map(int,input().split())
    mat=[[[] for _ in range(c)] for _ in range(r)]
    for _ in range(m):
        y,x,s,d,z=map(int,input().split())
        if d==1:d=0
        elif d==2:d=2
        elif d==3:d=1
        else:d=3
        mat[y-1][x-1]=[s,d,z]
    res=0
    for fisher_x in range(c):
        res+=fish(fisher_x)
        move()
    print(res)