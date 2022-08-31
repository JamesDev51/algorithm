import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def solve():
    global res, before
    for w,cnt in cube:
        before<<=3
        cube_length=pow(2,w)
        max_cnt=(length//cube_length)*(width//cube_length)*(height//cube_length)-before
        max_cnt=min(max_cnt,cnt)
        res+=max_cnt
        before+=max_cnt

        
if __name__=="__main__":
    length,width,height=map(int,input().split())
    n=int(input())
    cube=[list(map(int, input().split())) for _ in range(n)]
    cube.sort(reverse=True)
    res=0; before=0
    solve()
    print(res if before == length*width*height else -1)