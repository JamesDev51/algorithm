from collections import deque
def solution(board):
    answer = 0
    n=len(board)
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    que=deque([(0,0,1),(0,0,2)])
    cost=[[[0]*4 for _ in range(n)] for _ in range(n)]
    while que:
        y,x,d=que.popleft()
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if ny==0 and nx==0:continue
            if d==i:new_cost=100
            else:new_cost=600
            
            if 0<=ny<n and 0<=nx<n and (not cost[ny][nx][i] or 0<cost[y][x][d]+new_cost<cost[ny][nx][i]) and not board[ny][nx]:
                cost[ny][nx][i]=cost[y][x][d]+new_cost
                que.append((ny,nx,i))

    answer=float('inf')
    for tmp in cost[n-1][n-1]:
        if not tmp:continue
        answer=min(answer,tmp)
    return answer