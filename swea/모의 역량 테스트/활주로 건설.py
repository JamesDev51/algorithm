import sys
sys.stdin=open("input.text","rt")

def go():
    ret=0
    for y in range(n):
        flag=True
        ch=[0]*n
        height,acc=mat[y][0],0
        for x in range(n):
            if  (abs(mat[y][x]-height)>1):flag=False;break
            if height==mat[y][x]:acc+=1;continue
            elif mat[y][x]>height:
                if acc<k:flag=False;break
                else:
                    for _x in range(x-1,x-1-k,-1):
                        if not ch[_x]:ch[_x]=1
                        else:flag=False;break
            height=mat[y][x];acc=1
            
        if not flag:continue
        height,acc=mat[y][n-1],0
        for x in range(n-1,-1,-1):
            if  (abs(mat[y][x]-height)>1):flag=False;break
            if height==mat[y][x]:acc+=1;continue
            elif mat[y][x]>height:
                if acc<k:flag=False;break
                else:
                    for _x in range(x+1,x+1+k):
                        if not ch[_x]:ch[_x]=1
                        else:flag=False;break
            height=mat[y][x];acc=1
        if flag:ret+=1
        
    for x in range(n):
        flag=True
        ch=[0]*n
        height,acc=mat[0][x],0
        for y in range(n):
            if  (abs(mat[y][x]-height)>1):flag=False;break
            if height==mat[y][x]:acc+=1;continue
            elif mat[y][x]>height:
                if acc<k:flag=False;break
                else:
                    for _y in range(y-1,y-1-k,-1):
                        if not ch[_y]:ch[_y]=1
                        else:flag=False;break
            height=mat[y][x];acc=1
            
        if not flag:continue
        height,acc=mat[n-1][x],0
        for y in range(n-1,-1,-1):
            if  (abs(mat[y][x]-height)>1):flag=False;break
            if height==mat[y][x]:acc+=1;continue
            elif mat[y][x]>height:
                if acc<k:flag=False;break
                else:
                    for _y in range(y+1,y+1+k):
                        if not ch[_y]:ch[_y]=1
                        else:flag=False;break
            height=mat[y][x];acc=1
        if flag:ret+=1            
    return ret
        
for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(f"#{t} {go()}")
    