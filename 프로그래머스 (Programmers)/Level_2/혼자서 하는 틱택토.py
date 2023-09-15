def solution(board):
    answer = 1
    o_cnt=0
    x_cnt=0
    for y in range(3):
        for x in range(3):
            if board[y][x]=='O':o_cnt+=1
            if board[y][x]=='X':x_cnt+=1
    if abs(o_cnt-x_cnt)>1 or o_cnt<x_cnt:answer=0
    
    o_ttt=False
    x_ttt=False
    for y in range(3):
        row_set=set()
        for x in range(3):
            row_set.add(board[y][x])
        if len(row_set)==1:
            if 'O' in row_set:o_ttt=True
            if 'X' in row_set:x_ttt=True
    for x in range(3):
        col_set=set()
        for y in range(3):
            col_set.add(board[y][x])
        if len(col_set)==1:
            if 'O' in col_set:o_ttt=True
            if 'X' in col_set:x_ttt=True
    
    l_to_r=set()
    l_to_r.add(board[0][0])
    l_to_r.add(board[1][1])
    l_to_r.add(board[2][2])
    if len(l_to_r)==1:
        if 'O' in l_to_r:o_ttt=True
        if 'X' in l_to_r:x_ttt=True
    
    r_to_l=set()
    r_to_l.add(board[0][2])
    r_to_l.add(board[1][1])
    r_to_l.add(board[2][0])
    if len(r_to_l)==1:
        if 'O' in r_to_l:o_ttt=True
        if 'X' in r_to_l:x_ttt=True
    
    if o_ttt and x_ttt:
        answer=0
    if (o_ttt and not x_ttt) and o_cnt!=x_cnt+1:
        answer=0
    if (not o_ttt and x_ttt) and o_cnt!=x_cnt:
        answer=0
    if o_cnt+x_cnt==9 and o_cnt!=x_cnt+1:
        answer=0
                        
            
    return answer