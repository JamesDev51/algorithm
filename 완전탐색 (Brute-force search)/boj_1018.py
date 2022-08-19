import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    global res
    for sy in range(n-8+1):
        for sx in range(m-8+1):
            for color in range(2): #왼쪽 위가 B / W
                start='B' if color==0 else 'W'
                cnt=0
                for y in range(sy,sy+8):
                    prev=start
                    for x in range(sx,sx+8):
                        now=mat[y][x]
                        if prev==now: cnt+=1; prev='W' if prev=='B' else 'B'
                        else: prev=now
                    start='W' if start=='B' else 'B'
                res=min(res,cnt)

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(input().strip()) for _ in range(n)]
    res=1e9
    solve()
    print(res)