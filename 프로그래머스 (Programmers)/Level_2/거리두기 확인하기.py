from collections import deque
def bfs(place):
    que=deque()
    ch=[[0]*5 for _ in range(5)]
    for yy in range(5):
        for xx in range(5):
            if place[yy][xx]=='P':
                ch[yy][xx]=1
                que.append((yy,xx,0))
                while que:
                    y,x,dist=que.popleft()
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<5 and 0<=nx<5 and not ch[ny][nx] and place[ny][nx]!='X' and dist+1<=2:
                            if place[ny][nx]=='P': return 0
                            ch[ny][nx]=1
                            que.append((ny,nx,dist+1))
    return 1
                        
                    
            
def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer