import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solution():
    stack=[]
    stack2=[]
    largest=float('-inf')
    ans=0
    for height in heights:
        if largest<=height:
            while stack:ans+=(largest-stack.pop())
            largest=height
        stack.append(height)
    largest=float('-inf')
    for height in stack[::-1]:
        if largest<=height:
            while stack2:ans+=(largest-stack2.pop())
            largest=height
        stack2.append(height)
    return ans       

if __name__=="__main__":
    h,w=map(int,input().split())
    heights=list(map(int,input().split()))
    print(solution())
    