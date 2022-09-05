import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(ss):
    res="";
    stack=[]
    for s in ss:
        if s not in operators:res+=s
        else:
            if s=="+" or s=="-" or s=="*" or s=="/":
                while stack and stack[-1] not in "()" and  primitive[stack[-1]]>=primitive[s]:res+=stack.pop()
                stack.append(s)
            elif s=="(": stack.append(s); 
            elif s==")":
                while stack and stack[-1]!="(": res+=stack.pop()
                stack.pop()
    while stack: res+=stack.pop() 
    return res

if __name__=="__main__":
    operators="+-*/()"; primitive={"+":1,"-":1,"*":2,"/":2,"(":3}
    print(solve(input().strip()))