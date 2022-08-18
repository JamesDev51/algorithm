import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

'''
색이 다른 인접한 두칸 교환
행또는 열 가장 긴 것 먹기 (최대 개수는?)
'''
def check():
    global res
    acc_cnt=1
    for y in range(n):
        res=max(res,acc_cnt)
        acc_cnt=1;now=mat[y][0]
        for x in range(1,n):
            if now==mat[y][x]:acc_cnt+=1
            else: res=max(res,acc_cnt); now=mat[y][x];acc_cnt=1
    for x in range(n):
        res=max(res,acc_cnt)
        acc_cnt=1;now=mat[0][x]
        for y in range(1,n):
            if now==mat[y][x]:acc_cnt+=1
            else: res=max(res,acc_cnt); now=mat[y][x];acc_cnt=1
                
            

def solve():
    for y in range(n):
        for x in range(n):
            for dy,dx in zip([0,1],[1,0]):
                ny,nx=y+dy,x+dx
                if 0<=ny<n and 0<=nx<n and mat[y][x]!=mat[ny][nx]:
                    mat[y][x],mat[ny][nx]=mat[ny][nx],mat[y][x]
                    check()
                    mat[ny][nx],mat[y][x]=mat[y][x],mat[ny][nx]
                    



if __name__=="__main__":
    n=int(input())
    mat=[list(input().strip()) for _ in range(n)]

    res=float('-inf')
    solve()
    print(res)