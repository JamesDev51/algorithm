from collections import deque
def solution(maps):
    answer = []
    row,col=len(maps),len(maps[0])
    que=deque()
    ch=[[0]*col for _ in range(row)]
    
    for yy in range(row):
        for xx in range(col):
            if maps[yy][xx]!='X' and not ch[yy][xx]:
                que.append((yy,xx))
                ch[yy][xx]=1
                food=int(maps[yy][xx])
                while que:
                    y,x=que.popleft()
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<row and 0<=nx<col and maps[ny][nx]!='X' and not ch[ny][nx]:
                            ch[ny][nx]=1
                            food+=int(maps[ny][nx])
                            que.append((ny,nx))
                answer.append(food)
    answer.sort()
    return answer if answer else [-1]