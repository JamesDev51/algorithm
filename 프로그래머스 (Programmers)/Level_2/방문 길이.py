dy={'U':-1,'R':0,'D':1,'L':0}
dx={'U':0,'R':1,'D':0,'L':-1}

def solution(dirs):
    path=set()
    y,x=5,5
    for d in dirs:
        ny,nx=y+dy[d],x+dx[d]
        if 0<=ny<=10 and 0<=nx<=10:
            if (y,x,ny,nx) not in path and (ny,nx,y,x) not in path:
                path.add((y,x,ny,nx))
            y,x=ny,nx
        
        
    return len(path)