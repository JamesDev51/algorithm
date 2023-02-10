from collections import deque

def solution(maps):
    answer = 0
    row,col=len(maps),len(maps[0])
    ch=[[0]*col for _ in range(row)]
    ch[0][0]=1
    que=deque()
    que.append((0,0))
    
    while que:
        y,x=que.popleft()
        if y==row-1 and x==col-1:break
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<row and 0<=nx<col and maps[ny][nx]==1 and not ch[ny][nx]:
                ch[ny][nx]=ch[y][x]+1
                que.append((ny,nx))
    

    
    return ch[row-1][col-1] if ch[row-1][col-1]!=0 else -1