import sys
sys.stdin=open("input.text","rt")

def go():
    ay,ax=0,0
    by,bx=9,9
    res=0
    if mat[ay][ax]:res+=mat[ay][ax][0][0]
    if mat[by][bx]:res+=mat[by][bx][0][0]
    
    for time in range(m):
        ad=move_a[time]
        nay,nax=ay+dy[ad],ax+dx[ad]
        bd=move_b[time]
        nby,nbx=by+dy[bd],bx+dx[bd]
        
        plus_1=0
        ch=[0]*cnt
        for cap,idx in mat[nay][nax]:
            if not ch[idx]:plus_1+=cap;ch[idx]=1;break 
        for cap,idx in mat[nby][nbx]:
            if not ch[idx]:plus_1+=cap;ch[idx]=1;break 

        plus_2=0
        ch=[0]*cnt
        for cap,idx in mat[nby][nbx]:
            if not ch[idx]:plus_2+=cap;ch[idx]=1;break 
        for cap,idx in mat[nay][nax]:
            if not ch[idx]:plus_2+=cap;ch[idx]=1;break 
        res+=max(plus_1,plus_2)
        ay,ax=nay,nax
        by,bx=nby,nbx
    return res

dy,dx=[0,-1,0,1,0],[0,0,1,0,-1]
for t in range(1,int(input())+1):
    m,cnt=map(int,input().split())
    move_a=list(map(int,input().split()))
    move_b=list(map(int,input().split()))
    mat=[[[] for  _ in range(10)] for _ in range(10)]
    for idx in range(cnt):
        x,y,c,p=map(int,input().split())
        x-=1;y-=1
        for i in range(-c,c+1):
            for j in range(-c,c+1):
                ny,nx=y+i,x+j
                if not 0<=ny<10 or not 0<=nx<10:continue
                dist=abs(ny-y)+abs(nx-x)
                if dist<=c:mat[ny][nx].append((p,idx))
    for y in range(10):
        for x in range(10):
            mat[y][x].sort(key=lambda x:(-x[0],x[1]))
    print(f"#{t} {go()}")