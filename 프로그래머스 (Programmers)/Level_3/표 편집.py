def solution(n, k, cmd):
    answer = ''
    row_infos=[[0]*2 for _ in range(n)]
    for i in range(n):
        if 0<=i-1<n:row_infos[i][0]=i-1
        else:row_infos[i][0]=None
        
        if 0<=i+1<n:row_infos[i][1]=i+1
        else:row_infos[i][1]=None
    waste_stack=list()
    ch=['O']*n
    
    now_row=k
    
    for command in cmd:
        sp_command=command.split(" ")
        com=sp_command[0]
        
        if com in "UD":
            x=int(sp_command[1])
            while x:
                if com=="U":now_row=row_infos[now_row][0]
                else:now_row=row_infos[now_row][1]
                x-=1
                
        elif com=="C":
            up,down=row_infos[now_row]
            if up!=None:row_infos[up][1]=down
            if down!=None:row_infos[down][0]=up
            
            waste_stack.append(now_row)
            ch[now_row]='X'
            
            if down!=None:now_row=down
            else:now_row=up
            
        else:
            restore_row=waste_stack.pop()
            up,down=row_infos[restore_row]
            while up!=None and ch[up]=='X':up=row_infos[up][0]
            while down!=None and ch[down]=='X':down=row_infos[down][1]
            ch[restore_row]='O'
            
            if up!=None:
                row_infos[restore_row][0]=up
                row_infos[up][1]=restore_row
            else: #0번인 경우 up이 없음
                row_infos[restore_row][0]=None
                
            if down!=None:
                row_infos[restore_row][1]=down
                row_infos[down][0]=restore_row
            else:#n-1번인 경우 down이 없음
                row_infos[restore_row][1]=None
    answer=''.join(ch)
        

            
    return answer
 