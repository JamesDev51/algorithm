import sys
input=sys.stdin.readline

def check():
    ltor,rtol=0,0
    sumRow=[0]*3
    sumCol=[0]*3
    
    for y in range(3):
        for x in range(3):
            if y==x: ltor+=mat[y][x]
            if x==3-y-1: rtol+=mat[y][x]
            sumRow[y]+=mat[y][x]
            sumCol[x]+=mat[y][x]
    allValues=set(sumRow+sumCol+[ltor,rtol])
    if len(allValues)==1:
        print('YES')
        exit(0)
    
            

def dfs(idx):
    if idx==9:
        check()
        return
    for pos in range(9):
        if not ch[pos]:
            ch[pos]=1
            y,x=pos//3,pos%3
            mat[y][x]=a[idx]
            dfs(idx+1)
            ch[pos]=0
    

if __name__=="__main__":
    a=list(map(int,input().split()))
    mat=[[0]*3 for _ in range(3)]
    ch=[0]*9
    
    
    dfs(0)
    print("NO")