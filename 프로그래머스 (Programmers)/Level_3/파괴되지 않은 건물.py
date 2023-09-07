def solution(board, skill):
    answer = 0
    n,m=len(board),len(board[0])
    
    acc=[[0]*(m+1) for _ in range(n+1)]
    
    for t,r1,c1,r2,c2,degree in skill:
        if t==1:
            acc[r1][c1]-=degree
            acc[r1][c2+1]+=degree
            acc[r2+1][c1]+=degree
            acc[r2+1][c2+1]-=degree
        else:
            acc[r1][c1]+=degree
            acc[r1][c2+1]-=degree
            acc[r2+1][c1]-=degree
            acc[r2+1][c2+1]+=degree
    for y in range(n+1):
        for x in range(1,m+1):
            acc[y][x]+=acc[y][x-1]
    for x in range(m+1):
        for y in range(1,n+1):
            acc[y][x]+=acc[y-1][x]

    for y in range(n):
        for x in range(m):
            board[y][x]+=acc[y][x]
            if board[y][x]>0:answer+=1
        
    
    return answer