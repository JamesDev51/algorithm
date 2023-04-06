import sys
sys.stdin=open("input.text","rt")

def make_block():
    block=dict()
    block[1]=dict()
    block[1][0]=2;block[1][1]=3;block[1][3]=0;block[1][2]=1
    
    block[2]=dict()
    block[2][0]=1;block[2][1]=3;block[2][2]=0;block[2][3]=2
    
    block[3]=dict()
    block[3][1]=2;block[3][0]=3;block[3][2]=0;block[3][3]=1
    
    block[4]=dict()
    block[4][0]=2;block[4][1]=0;block[4][2]=3;block[4][3]=1
    return block
    
    

def make_warmhole():
    warmhole=dict()
    for y in range(n):
        for x in range(n):
            num=mat[y][x]
            if 6<=num<=10:
                if num in warmhole:warmhole[num].append((y,x))
                else:warmhole[num]=[(y,x)]
    return warmhole
                
def go(sy,sx,d):
    score=0
    y,x=sy,sx
    while True:
        while True:
            ny,nx=y+dy[d],x+dx[d]
            if (ny,nx)==(sy,sx):
                return score
            if 0<=ny<n and 0<=nx<n and mat[ny][nx]==0:y,x=ny,nx #빈곳으로 무빙
            else:break #이외의 블록, 웜홀, 블랙홀, 벽
        if not 0<=ny<n or not 0<=nx<n: #벽인 경우
            score+=1
            d=(d+2)%4
            y,x=ny,nx
        elif mat[ny][nx]==5:
            score+=1
            d=(d+2)%4
            y,x=ny,nx
        elif 1<=mat[ny][nx]<=4: #블록
            score+=1
            d=block[mat[ny][nx]][d]
            y,x=ny,nx
        elif 6<=mat[ny][nx]<=10: #웜홀
            cord1,cord2 = warmhole[mat[ny][nx]]
            if (ny,nx)==cord1:y,x=cord2
            else:y,x=cord1
        elif mat[ny][nx]==-1:
            return score
block=make_block()
dy,dx=[-1,0,1,0],[0,1,0,-1]
for t in range(1,int(input())+1):
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    warmhole=make_warmhole()
    res=-1e9
    for sy in range(n):
        for sx in range(n):
            for d in range(4):
                if mat[sy][sx]==0:
                    res=max(res,go(sy,sx,d))
    print(f"#{t} {res}")