import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def go():
    ret=0
    ch=[[[0]*4 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        flag=True
        for x in range(1,n):
            if abs(mat[y][x-1]-mat[y][x])>1:flag=False;break #높이 차이가 1 초과
            elif mat[y][x-1]-1==mat[y][x]: #낮아지는 경우
                now=mat[y][x]
                for i in range(l):
                    if x+i<n and mat[y][x+i]==now and not ch[y][x+i][1] and not ch[y][x+i][3]:ch[y][x+i][1]=1
                    else:flag=False;break    
        if not flag:continue
        acc=0
        for x in range(n-2,-1,-1):
            if abs(mat[y][x+1]-mat[y][x])>1:flag=False;break #높이 차이가 1 초과
            elif mat[y][x+1]-1==mat[y][x]: #다음이 더 낮은 경우
                now=mat[y][x]
                for i in range(l):
                    if 0<=x-i and mat[y][x-i]==now and not ch[y][x-i][1] and not ch[y][x-i][3]:ch[y][x-i][3]=1
                    else:flag=False;break 
        if not flag:continue
        ret+=1
        
    for x in range(n):
        flag=True
        for y in range(1,n):
            if abs(mat[y-1][x]-mat[y][x])>1:flag=False;break #높이 차이가 1 초과
            elif mat[y-1][x]-1==mat[y][x]: #낮아지는 경우
                now=mat[y][x]
                for i in range(l):
                    if y+i<n and mat[y+i][x]==now and not ch[y+i][x][0] and not ch[y+i][x][2]:ch[y+i][x][2]=1
                    else:flag=False;break    
        if not flag:continue
        acc=0
        for y in range(n-2,-1,-1):
            if abs(mat[y+1][x]-mat[y][x])>1:flag=False;break #높이 차이가 1 초과
            elif mat[y+1][x]-1==mat[y][x]: #다음이 더 낮은 경우
                now=mat[y][x]
                for i in range(l):
                    if 0<=y-i and mat[y-i][x]==now and not ch[y-i][x][0] and not ch[y-i][x][2]:ch[y-i][x][0]=1
                    else:flag=False;break 
        if not flag:continue
        ret+=1

    return ret

if __name__=="__main__":
    n,l=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(go())
    