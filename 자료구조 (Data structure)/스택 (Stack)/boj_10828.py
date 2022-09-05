import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n=int(input())
    stack=[]
    for _ in range(n):
        com=input().strip()
        if "push" in com:
            push,num=com.split()
            stack.append(num)
        elif "pop" ==com:print(stack.pop() if stack else -1)
        elif "size"==com:print(len(stack))
        elif "empty"==com: print(1 if not stack else 0)
        elif "top"==com:print(stack[-1] if stack else -1)