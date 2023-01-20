import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def acc():
    for x in range(1,101):
        for y in range(1,101):
            if mat[y][x]:mat[y][x]+=mat[y-1][x]

def solve():
    answer=100
    stack=[]
    for y in range(1,101):
        stack.append(0)
        for x in range(1,102):
            while stack and mat[y][x]<mat[y][stack[-1]]:
                then_x=stack.pop()
                height=mat[y][then_x]
                answer=max(answer, height*(x-then_x)) #넓이 갱신
            stack.append(x)
    return answer

            
if __name__=="__main__":
    n=int(input())
    mat=[[0]*102 for _ in range(101)]
    for _ in range(n):
        left,top=map(int,input().split())
        for y in range(top,top+10):
            for x in range(left,left+10):
                mat[y][x]=1
    acc()
    print(solve())
    
        