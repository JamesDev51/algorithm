import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(size_limit):
    global res
    if sum(used)>=res: return #같거나 더 많이 썻으면 더 볼필요 없음
    for size in range(size_limit,6):
        for sy in range(10):
            for sx in range(10):
                tmp_sum=0
                if sy+size<=10 and sx+size<=10: #확인해 볼 수 있는곳
                    for y in range(sy,sy+size):
                        for x in range(sx,sx+size):
                            tmp_sum+=mat[y][x]
                    if tmp_sum==pow(size,2) and used[size]<=4: #붙일 수 있는 곳
                        used[size]+=1
                        for y in range(sy,sy+size):
                            for x in range(sx,sx+size):
                                mat[y][x]=0
                        dfs(size) #붙이고 일단 다음 단계로 이동
                        used[size]-=1
                        for y in range(sy,sy+size):
                            for x in range(sx,sx+size):
                                mat[y][x]=1
    for q in mat:print(q)
    print()
    if sum(sum(mat[i]) for i in range(10))==0:
        res=min(res,sum(used))
                        

if __name__=="__main__":
    mat=[list(map(int,input().split())) for _ in range(10)]
    res=float('inf')
    used=[0]*6
    dfs(1)
    print(res if res!=float('inf') else -1)