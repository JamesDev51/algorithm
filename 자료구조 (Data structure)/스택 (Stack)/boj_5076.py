import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(codes):
    stack=[]
    tmp="";flag=False
    for c in codes:
        if c=="<": tmp="<"; flag=True
        elif c==">": 
            tmp+=">"; flag=False; 
            if tmp=="<br />":continue
            elif tmp[1]=="/" and stack and stack[-1][1:len(tmp)-2]==tmp[2:-1]:stack.pop()
            else:stack.append(tmp)
        else:
            if flag:tmp+=c
            else: tmp=""
    return "legal" if not stack else "illegal"
if __name__=="__main__":
    while True:
        codes=input().strip()
        if codes=="#":break
        print(solve(codes))