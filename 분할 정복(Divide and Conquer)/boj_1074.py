import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(u,d,l,r):
    global cnt,row,col
    if d-u==2 and r-l==2:
        for y in range(u,d):
            for x in range(l,r):
                if y==row and x==col: print(cnt);exit(0)
                cnt+=1
    else:
        for sy in range(u,d,(d-u)//2):
            for sx in range(l,r,(r-l)//2):
                if sy<=row<sy+(d-u)//2 and sx<=col<sx+(r-l)//2:
                    solve(sy,sy+(d-u)//2,sx,sx+(r-l)//2)
                else:
                    cnt+=((d-u)*(r-l))//4
                    


if __name__=="__main__":
    n,row,col=map(int,input().split())
    cnt=0
    solve(0,1<<n,0,1<<n)
