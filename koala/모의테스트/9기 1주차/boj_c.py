import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


def init():
    for _ in range(int(input())):
        left,bottom=map(int,input().split())
        for y in range(bottom,bottom+10):
            for x in range(left,left+10):
                paper[y][x]=1

def acc():
    for y in range(1,101):
        for x in range(1,101):
            if paper[y][x]: paper[y][x]+=paper[y-1][x]

def solve():
    answer=100
    for y in range(1,101):
        stack=[0]
        for x in range(1,102):
            while stack and paper[y][x]<paper[y][stack[-1]]:
                then_x=stack.pop()
                height=paper[y][then_x]
                answer=max(answer,height*(x-1-stack[-1]))
            stack.append(x)
    return answer

            
if __name__=="__main__":
    paper=[[0]*102 for _ in range(101)]
    init()
    acc()
    print(solve())