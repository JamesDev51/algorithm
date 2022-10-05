import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(x):
    global res
    if x==n: res+=1
    else:
        for y in range(n):
            if not (row[y] or ltr[y-x] or rtl[y+x]):
                row[y]=ltr[y-x]=rtl[y+x]=1
                dfs(x+1)
                row[y]=ltr[y-x]=rtl[y+x]=0
            
if __name__=="__main__":
    n=int(input())
    row=[0]*n
    ltr=[0]*(2*n-1)
    rtl=[0]*(2*n-1)
    res=0
    dfs(0)
    print(res)