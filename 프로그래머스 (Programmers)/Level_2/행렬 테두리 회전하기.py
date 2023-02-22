from collections import deque
que=deque()

def init(mat,rows,columns):
    num=1
    for y in range(1,rows+1):
        for x in range(1,columns+1):
            mat[y][x]=num;num+=1;

def move(mat,y1,x1,y2,x2):
    for x in range(x1,x2):que.append(mat[y1][x])
    for y in range(y1,y2):que.append(mat[y][x2])
    for x in range(x2,x1,-1):que.append(mat[y2][x])
    for y in range(y2,y1,-1):que.append(mat[y][x1])
    ret=min(que)
    for x in range(x1+1,x2+1):mat[y1][x]=que.popleft()
    for y in range(y1+1,y2+1):mat[y][x2]=que.popleft()
    for x in range(x2-1,x1-1,-1):mat[y2][x]=que.popleft()
    for y in range(y2-1,y1-1,-1):mat[y][x1]=que.popleft()
    return ret

    
def solution(rows, columns, queries):
    answer = []
    mat=[[0]*(columns+1) for _ in range(rows+1)]
    init(mat,rows, columns)
    for y1,x1,y2,x2 in queries:
        answer.append(move(mat,y1,x1,y2,x2))
    
    return answer