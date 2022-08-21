import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(1e9)
input=sys.stdin.readline

def solve(l,w,h):
    global res
    if not l or not w or not h: return #셋중 하나라도 끝났으면 종료
    for i in range(19,0,-1):
        if not info[i]: continue
        cube_length=1<<i
        if info[i]>0 and cube_length<=l and cube_length<=w and cube_length<=h:
            info[i]-=1
            res+=1
            solve(l-cube_length,cube_length,h)
            solve(cube_length,cube_length,h-cube_length)
            solve(l,w-cube_length,h)
            break
    else: return
        
        
        

if __name__=="__main__":
    length,width,height=map(int,input().split())
    n=int(input())
    info=[0]*20
    for _ in range(n):a,b=map(int,input().split()); info[a]=b
    res=0
    #큰 순서대로 채워야 됨
    #분할정복으로 쪼개면서 내려감
    solve(length,width,height) 
    print(res)