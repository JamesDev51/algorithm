import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(word):
    stack=[]
    for s in word:
        if not stack: stack.append(s)
        else:
            if stack[-1]==s:stack.pop()
            else:stack.append(s)
    return True if not stack else False

if __name__=="__main__":
    res=0
    n=int(input())
    for _ in range(n):
        if solve(input().strip()):res+=1
    print(res)