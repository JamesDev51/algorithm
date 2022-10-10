import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check():
    lt,rt=len(res)-2,len(res)-1
    while 0<=lt:
        if res[lt:rt]==res[rt:]: return False
        lt-=2; rt-=1
    return True

def dfs(l):
    if l==n:
        print(''.join(res))
        exit(0)
    else:
        for i in range(1,4):
            res.append(str(i))
            if check():
                dfs(l+1)
            res.pop()        
if __name__=="__main__":
    n=int(input())
    res=list()
    dfs(0)
