import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(u,d,l,r):
    if u+1==d and l+1==r: res[u][l]="*";return
    cnt=0
    for sy in range(u,d,(d-u)//3):
        for sx in range(l,r,(r-l)//3):
            if cnt==4: cnt+=1;continue
            solve(sy,sy+(d-u)//3,sx,sx+(r-l)//3)
            cnt+=1

if __name__=="__main__":
    n=int(input())
    res=[[" "]*n for _ in range(n)]
    solve(0,n,0,n)
    for row in res:
        for val in row:
            print(val,end="")
        print()



'''
***
* *
***
'''