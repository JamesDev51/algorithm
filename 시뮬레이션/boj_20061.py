import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def green(t,y,x):
    ret=0
    cols=[x]
    if t==2:cols.append(x+1)
    
    #아래 블록이 없을때까지 계속 내려가기
    now_row=3
    while now_row<9:
        flag=True
        for col in cols:
            if mat[now_row+1][col]==1:flag=False
        if not flag:break
        else:now_row+=1
    
    #블럭 놓기
    mat[now_row][x]=1
    if t==2:mat[now_row][x+1]=1
    elif t==3:mat[now_row-1][x]=1
    #점수 획득하기
    y=9
    while y>3:
        cnt=0
        for x in range(4): cnt+=mat[y][x]
        if cnt==4: #가득 참
            ret+=1
            for x in range(4):mat[y][x]=0
            for _y in range(y-1,3,-1):
                for x in range(4):
                    mat[_y+1][x],mat[_y][x]=mat[_y][x],mat[_y+1][x]
        else:
            y-=1
    #옅은 색 차있는 갯수 구하기
    cnt=0
    for y in range(4,6):
        for x in range(4):
            if mat[y][x]:cnt+=1;break
    #아래부터 없애면서 끌어 내리기
    for _ in range(cnt):
        for x in range(4):
            mat[9][x]=0
        for _y in range(8,3,-1):
            for x in range(4):
                mat[_y+1][x],mat[_y][x]=mat[_y][x],mat[_y+1][x]
    return ret

def blue(t,y,x):
    ret=0
    rows=[y]
    if t==3:rows.append(y+1)
    #오른쪽 블록이 없을때까지 계속 내려가기
    now_col=3
    while now_col<9:
        flag=True
        for row in rows:
            if mat[row][now_col+1]==1:flag=False
        if not flag:break
        else:now_col+=1
    #블럭 놓기
    mat[y][now_col]=1
    if t==2:mat[y][now_col-1]=1
    elif t==3:mat[y+1][now_col]=1
    
    #점수 획득하기
    x=9
    while x>3:
        cnt=0
        for y in range(4): cnt+=mat[y][x]
        if cnt==4: #가득 참
            ret+=1
            for y in range(4):mat[y][x]=0
            for _x in range(x-1,3,-1):
                for y in range(4):
                    mat[y][_x+1],mat[y][_x]=mat[y][_x],mat[y][_x+1]
        else:
            x-=1
        
    #옅은 색 차있는 갯수 구하기
    cnt=0
    for x in range(4,6):
        for y in range(4):
            if mat[y][x]:cnt+=1;break
            
    #아래부터 없애면서 끌어 내리기
    for x in range(cnt):
        for y in range(4):
            mat[y][9]=0
        for _x in range(8,3,-1):
            for y in range(4):
                mat[y][_x],mat[y][_x+1]=mat[y][_x+1],mat[y][_x]        
    return ret

def count_left_cnt():
    ret=0
    for y in range(4):
        for x in range(6,10):
            ret+=mat[y][x]
    for y in range(6,10):
        for x in range(4):
            ret+=mat[y][x]
    return ret
            
    

if __name__=="__main__":
    mat=[[0]*10 for _ in range(10)]
    score=0
    n=int(input())
    for _ in range(n):
        t,y,x=map(int,input().split())
        score+=green(t,y,x)
        score+=blue(t,y,x)
    left_cnt=count_left_cnt()
    print(score)
    print(left_cnt)