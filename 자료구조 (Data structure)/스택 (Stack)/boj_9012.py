import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(ss):
    stack=[]
    for s in ss:
        if s=="(":stack.append(s)
        elif s==")" and stack and stack[-1]=="(":stack.pop()
        else: return "NO"
    return "YES" if not stack else "NO"

if __name__=="__main__":
    for _ in range(int(input())):
        print(solve(input().strip()))