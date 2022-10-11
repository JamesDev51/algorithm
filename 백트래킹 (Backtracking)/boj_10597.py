import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(idx):
    if len(res)==size:
        print(*res)
        exit(0)
    else:
        if s[idx]!=0:
            num_1=int(s[idx])
            if 1<=num_1<=size and num_1 not in res:
                res.append(num_1)
                dfs(idx+1)
                res.pop()
            num_2=int(s[idx:idx+2])
            if 1<=num_2<=size and num_2 not in res:
                res.append(num_2)
                dfs(idx+2)
                res.pop() 

if __name__=="__main__":
    s=input().strip()
    l=0; size=0
    for i in range(1,51):
        l+=len(str(i))
        if l==len(s):size=i;break
    res=list()
    dfs(0)