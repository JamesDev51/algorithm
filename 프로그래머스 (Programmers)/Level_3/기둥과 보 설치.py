mat=None

def check_add_pillar(x,y):
    #바닥 위
    if y==0:return True
    #보의 한쪽 끝 위
    if mat[x][y][1] or mat[x-1][y][1]:return True
    #다른 기둥 위
    if mat[x][y-1][0]:return True
    return False

def check_add_roof(x,y):
    #한쪽 끝이 기둥 위
    if mat[x][y-1][0] or mat[x+1][y-1][0]:return True
    #양쪽 끝이 다른 보와 동시 연결
    if mat[x-1][y][1] and mat[x+1][y][1]:return True
    return False

def check_remove_pillar(n,x,y):
    mat[x][y][0]=0
    flag=True
    for dx in range(-3,4):
        for dy in range(-3,4):
            nx,ny=x+dx,y+dy
            if 0<=nx<=n and 0<=ny<=n:
                if mat[nx][ny][0]:
                    if not check_add_pillar(nx,ny):flag=False;break

                if mat[nx][ny][1]:
                    if not check_add_roof(nx,ny):flag=False;break
                    
    if not flag:mat[x][y][0]=1
        
def check_remove_roof(n,x,y):
    mat[x][y][1]=0
    flag=True
    for dx in range(-3,4):
        for dy in range(-3,4):
            nx,ny=x+dx,y+dy
            if 0<=nx<=n and 0<=ny<=n:
                if mat[nx][ny][0]:
                    if not check_add_pillar(nx,ny): flag=False;break

                if mat[nx][ny][1]:
                    if not check_add_roof(nx,ny):flag=False;break
    if not flag:mat[x][y][1]=1

def solution(n, build_frame):
    global mat
    answer = []
    mat=[[[0]*2 for _ in range(n+1)] for _ in range(n+1)]
    
    for x,y,a,b in build_frame:
        if b==0: #삭제
            if a==0: #기둥
                check_remove_pillar(n,x,y)
            else: #보
                check_remove_roof(n,x,y)
        else: #설치
            if a==0: #기둥
                if check_add_pillar(x,y):
                    mat[x][y][0]=1
            else: #보
                if check_add_roof(x,y):
                    mat[x][y][1]=1
    for x in range(n+1):
        for y in range(n+1):
            if mat[x][y][0]:answer.append([x,y,0])
            if mat[x][y][1]:answer.append([x,y,1])
    return answer