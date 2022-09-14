import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline

def solve():
    stack=[]
    for y in range(n):
        for x in range(n):
            if mat[y][x] and not ch[y][x]:
                size=1
                ch[y][x]=1
                stack.append((y,x))
                while stack:
                    yy,xx=stack.pop()    
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=yy+dy,xx+dx
                        if 0<=ny<n and 0<=nx<n and mat[ny][nx] and not ch[ny][nx]:
                            ch[ny][nx]=1
                            size+=1
                            stack.append((ny,nx))
                heapq.heappush(heap,size)                


if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().strip())) for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    heap=[]
    solve()
    print(len(heap))
    while heap: print(heapq.heappop(heap))