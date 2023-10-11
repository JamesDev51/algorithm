import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def lotate_sticker(r,c,sticker):
    lotated_sticker=[[0]*r for _ in range(c)]
    for y in range(r):
        for x in range(c):
            lotated_sticker[x][r-y-1]=sticker[y][x]
    return lotated_sticker
        
    

def find_sticker_location(r,c,sticker):
    for _ in range(4):
        if r<=n and c<=m:
            for sy in range(n-r+1):
                for sx in range(m-c+1):
                    flag=True
                    for my in range(r):
                        for mx in range(c):
                            y,x=sy+my,sx+mx
                            
                            if sticker[my][mx] and mat[y][x]:flag=False
                    if flag:
                        for my in range(r):
                            for mx in range(c):
                                y,x=sy+my,sx+mx
                                if sticker[my][mx]:
                                    mat[y][x]=sticker[my][mx]
                        return
        lotated_sticker=lotate_sticker(r,c,sticker)
        r,c=c,r
        sticker=lotated_sticker
        
if __name__=="__main__":
    n,m,k=map(int,input().split())
    mat=[[0]*m for _ in range(n)]
    for _ in range(k):
        r,c=map(int,input().split())
        sticker=[list(map(int,input().split())) for _ in range(r)]
        find_sticker_location(r,c,sticker)
    answer=0
    for y in range(n):
        for x in range(m):
            answer+=mat[y][x]
    print(answer)