def solution(keyinput, board):
    answer = [0,0]
    moves=["up","right","down","left"]
    dx,dy=[0,1,0,-1],[1,0,-1,0]
    for keyIn in keyinput:
        idx=moves.index(keyIn)
        nx,ny=answer[0]+dx[idx],answer[1]+dy[idx]
        if abs(nx)<=board[0]//2:answer[0]=nx
        if abs(ny)<=board[1]//2:answer[1]=ny

    return answer