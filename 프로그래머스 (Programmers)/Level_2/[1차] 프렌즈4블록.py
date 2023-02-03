from collections import deque

mat=[]
que=deque()

def has_exploded(m,n):
    ch=[[0]*n for _ in range(m)]
    for y in range(m-1):
        for x in range(n-1):
            if mat[y][x]==mat[y][x+1]==mat[y+1][x]==mat[y+1][x+1]!='':
                que.append((y,x))
                que.append((y,x+1))
                que.append((y+1,x))
                que.append((y+1,x+1))
    return len(que)
            
                
            
def explode():
    s=set()
    while que:
        y,x=que.popleft()
        s.add((y,x))
        mat[y][x]=''
    return len(s)
        

def gravity(m,n):
    for x in range(n):
        last_y=m-1
        for y in range(m-1,-1,-1):
            if mat[y][x]!='':
                mat[last_y][x],mat[y][x]=mat[y][x],mat[last_y][x]
                last_y-=1
            
    
def solution(m, n, board):
    global mat
    answer = 0
    for i in range(m):mat.append(list(board[i]))
    
    
    while has_exploded(m,n):
        answer+=explode()
        gravity(m,n)
        

    return answer