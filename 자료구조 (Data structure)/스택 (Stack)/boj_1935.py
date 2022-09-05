import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    stack=[]
    operators="+-*/"
    for s in ss:
        if s not in operators:stack.append(alpha_num[s])
        else:
            up=stack.pop()
            down=stack.pop()
            if s=="+": stack.append(down+up)
            elif s=="-": stack.append(down-up)
            elif s=="*": stack.append(down*up)
            elif s=="/":stack.append(down/up)
    return stack[-1]    
if __name__=="__main__":
    n=int(input())    
    ss=input().strip()
    alpha_num=dict()
    for i in range(65,65+n): alpha_num[chr(i)]=int(input())
    print(f"{solve():.2f}")