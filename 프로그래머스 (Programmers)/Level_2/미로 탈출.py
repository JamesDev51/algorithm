from collections import deque
def solution(maps):
    answer = -1
    que=deque()
    row=len(maps);col=len(maps[0])
    for y in range(row):
        for x in range(col):
            if maps[y][x]=='S':sy,sx=y,x
            elif maps[y][x]=='E':ey,ex=y,x
            elif maps[y][x]=='L':ly,lx=y,x
            
    ch=[[0]*col for _ in range(row)];ch[sy][sx]=1
    que.append((sy,sx,0))
    dist1=0
    dist2=0
    while que:
        y,x,cnt=que.popleft()
        if (y,x)==(ly,lx):
            que.clear()
            dist1=cnt;break
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<row and 0<=nx<col and not ch[ny][nx] and maps[ny][nx]!='X':
                ch[ny][nx]=1
                que.append((ny,nx,cnt+1))
    if dist1:    
        ch=[[0]*col for _ in range(row)];ch[ly][lx]=1
        que.append((ly,lx,0))
        while que:
            y,x,cnt=que.popleft()
            if (y,x)==(ey,ex):
                que.clear()
                dist2=cnt;break
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<row and 0<=nx<col and not ch[ny][nx] and maps[ny][nx]!='X':
                    ch[ny][nx]=1
                    que.append((ny,nx,cnt+1))
        
    if dist1 and dist2:
        answer=dist1+dist2
            
    
    return answer