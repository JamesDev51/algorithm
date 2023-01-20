def init(board,n):
    top_idx=[n]*n
    for x in range(n):
        for y in range(n):
            if board[y][x]:top_idx[x]=y;break
    return top_idx

def solve(board,moves,n,top_idx):
    answer=0
    stack=[]
    for move in moves:
        if top_idx[move-1]<n:
            doll=board[top_idx[move-1]][move-1]
            board[top_idx[move-1]][move-1]=0
            top_idx[move-1]+=1
            if stack and stack[-1]==doll: stack.pop();answer+=2
            else:stack.append(doll)
    return answer            
            

def solution(board, moves):
    answer = 0
    n=len(board)
    top_idx=init(board,n)
    answer=solve(board,moves,n,top_idx)
    return answer