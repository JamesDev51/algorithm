def solution(board):
    answer = 0
    n=len(board)
    for y in range(n):
        for x in range(n):
            if board[y][x]==1:
                for dy,dx in zip([-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]):
                    ny,nx=y+dy,x+dx
                    if 0<=ny<n and 0<=nx<n and board[ny][nx]==0:
                        board[ny][nx]=2
    for y in range(n):
        for x in range(n):
            if board[y][x]==0:answer+=1
                    
                
    return answer