from collections import deque
cells=[['']*51 for _ in range(51)]
cells_parents=dict()

def get_parents(r,c):
    if cells_parents[(r,c)]==(r,c):return (r,c)
    pr,pc=cells_parents[(r,c)]
    return get_parents(pr,pc)

def change_value(r,c,val):
    pr,pc=get_parents(r,c)
    cells[pr][pc]=val

def replace_value(val1,val2):
    que=deque()
    for y in range(51):
        for x in range(51):
            pr,pc=get_parents(y,x)
            if cells[pr][pc]==val1:que.append((y,x))
    while que:
        r,c=que.popleft()
        cells[r][c]=val2
            
def merge(r1,c1,r2,c2):
    pr1,pc1=get_parents(r1,c1)
    pr2,pc2=get_parents(r2,c2)
    if (pr1,pc1)==(pr2,pc2):return
    if cells[pr1][pc1]=='' and cells[pr2][pc2]!='':pr1,pc1,pr2,pc2=pr2,pc2,pr1,pc1
    
    
    que=deque()
    for y in range(51):
        for x in range(51):
            py,px=get_parents(y,x)
            if (py,px)==(pr2,pc2):que.append((y,x))
    while que:
        r,c=que.popleft()
        cells[r][c]=''
        cells_parents[(r,c)]=(pr1,pc1)
        
def unmerge(r,c):
    pr,pc=get_parents(r,c)
    val_copy=cells[pr][pc]
    
    que=deque()
    for y in range(51):
        for x in range(51):
            py,px=get_parents(y,x)
            if (py,px)==(pr,pc):
                que.append((y,x))
    while que:
        rr,cc=que.popleft()
        cells_parents[(rr,cc)]=(rr,cc)
        cells[rr][cc]=''
        if (rr,cc)==(r,c):cells[rr][cc]=val_copy
            
        
        
    
def solution(commands):
    answer = []
    for y in range(51):
        for x in range(51):
            cells_parents[(y,x)]=(y,x)
    
    
    for command in commands:
        splited=command.split(" ")
        if splited[0]=='UPDATE' and len(splited)==4:
            r,c=map(int,splited[1:3])
            val=splited[3]
            change_value(r,c,val) 
            
        elif splited[0]=='UPDATE' and len(splited)==3:
            val1,val2=splited[1:]
            replace_value(val1,val2)
            
        elif splited[0]=='MERGE':
            r1,c1,r2,c2=map(int,splited[1:])
            merge(r1,c1,r2,c2)
            
        elif splited[0]=='UNMERGE':
            r,c=map(int,splited[1:])
            unmerge(r,c)
            
        else: #print
            r,c=map(int,splited[1:])
            pr,pc=get_parents(r,c)
            val=cells[pr][pc]
            if val=='':answer.append('EMPTY')
            else:answer.append(val)
            
    return answer