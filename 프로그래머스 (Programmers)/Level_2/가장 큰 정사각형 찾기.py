def solution(board):
    board.insert(0,[0]*(len(board[0])))
    for y in range(len(board)): board[y].insert(0,0);board[y].append(0)
    
    row=len(board); col=len(board[0])
    acc_board=[[0]*(col) for _ in range(row)]
    
    for x in range(1,col):
        for y in range(1,row):
            if board[y][x]==0:continue
            acc_board[y][x]=acc_board[y-1][x]+board[y][x] 
    
    answer=0
    for y in range(row-1,0,-1):
        stack=list(); stack.append((0,0))
        for x in range(1,col):
            largest=float('inf');cnt=0
            while stack and stack[-1][0]>acc_board[y][x]:
                poped,poped_idx=stack.pop()
                cnt+=(poped_idx-stack[-1][1])
                largest=min(largest,poped)
                if cnt>=largest:answer=max(answer,largest*largest)
            
            stack.append((acc_board[y][x],x))
    return answer