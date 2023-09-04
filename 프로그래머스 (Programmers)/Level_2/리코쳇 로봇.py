from collections import deque
def find_robot(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]=='R':return (y,x)
def find_exit(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]=='G':return (y,x)

        
def solution(board):
    n,m=len(board),len(board[0])
    ry,rx=find_robot(board)
    gy,gx=find_exit(board)
    ch=[[0]*m for _ in range(n)]
    answer = -1
    que=deque()
    que.append((ry,rx,0))
    ch[ry][rx]=1
    while que:
        y,x,cnt=que.popleft()
        if (y,x)==(gy,gx):
            answer=cnt
            break
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            cy,cx=y,x
            while 0<=cy+dy<n and 0<=cx+dx<m and board[cy+dy][cx+dx] in '.GR':
                cy+=dy;cx+=dx
            if not ch[cy][cx]:
                ch[cy][cx]=1
                que.append((cy,cx,cnt+1))
    
    return answer