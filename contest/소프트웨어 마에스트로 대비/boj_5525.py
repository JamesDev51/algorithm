import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def make_p(n):
    return "I"+"OI"*n

if __name__=="__main__":
    n=int(input())
    m=int(input())
    s=input().strip()
    idx=1;tmp=0
    res=0
    while idx<len(s)-1:
        if s[idx-1]=='I' and s[idx]=='O' and s[idx+1]=='I':
            tmp+=1
            idx+=1
        else:tmp=0
        if tmp==n:res+=1;tmp-=1
        idx+=1
    print(res)