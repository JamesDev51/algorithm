import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

dice=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]]
d_converter={1:1,2:3,3:0,4:2}
dy,dx=[-1,0,1,0],[0,1,0,-1]

def up():
    tmp=[]
    for i in range(4):tmp.append(dice[i][1])
    tmp=tmp[1:]+[tmp[0]]
    for i in range(4):dice[i][1]=tmp[i]
    
def down():
    tmp=[]
    for i in range(4):tmp.append(dice[i][1])
    tmp=[tmp[-1]]+tmp[:-1]
    for i in range(4):dice[i][1]=tmp[i]
    
def right():
    dice[1][2],dice[3][1]=dice[3][1],dice[1][2]
    dice[1].insert(0,dice[1].pop())
    
def left():
    dice[1][0],dice[3][1]=dice[3][1],dice[1][0]
    dice[1].append(dice[1].pop(0))
    
def go():
    global y,x
    for d in move_plans:
        converted_d=d_converter[d]
        ny,nx=y+dy[converted_d],x+dx[converted_d]
        if not 0<=ny<n or not 0<=nx<m:continue
        if converted_d==0:up()#북
        elif converted_d==1:right()#동
        elif converted_d==2:down()#남
        else:left()#서
        y,x=ny,nx
        if mat[y][x]==0:mat[y][x]=dice[3][1]
        else:dice[3][1]=mat[y][x];mat[y][x]=0
        print(dice[1][1])

if __name__=="__main__":
    n,m,y,x,k=map(int,input().split())
    mat=[list(map(int, input().split())) for _ in range(n)]
    move_plans=list(map(int,input().split()))
    go()