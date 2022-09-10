import sys
from turtle import left
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    res=0
    left_stack,right_stack=[],[]
    for i in range(n):
        if not left_stack: left_stack.append(sticks[i])
        elif left_stack and left_stack[-1][1]<=sticks[i][1]:
            res+=left_stack[-1][1]*(sticks[i][0]-left_stack[-1][0])
            left_stack.append(sticks[i])
    for i in range(n-1,-1,-1):
        if not right_stack: right_stack.append(sticks[i])
        elif right_stack and right_stack[-1][1]<=sticks[i][1]:
            res+=right_stack[-1][1]*(right_stack[-1][0]-sticks[i][0])
            right_stack.append(sticks[i])
    res+=left_stack[-1][1]*(right_stack[-1][0]-left_stack[-1][0]+1)
    return res
        
    
    
if __name__=="__main__":
    n=int(input())
    sticks=[list(map(int,input().split())) for _ in range(n)]
    sticks.sort(key=lambda x : (x[0]))
    print(solve())
        