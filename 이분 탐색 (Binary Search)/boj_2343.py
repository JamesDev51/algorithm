import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(limit):
    cnt=1; tmp_sum=0
    for file in files:
        if tmp_sum+file<=limit:tmp_sum+=file
        else:cnt+=1; tmp_sum=file
    return True if cnt<=m else False
            

def solve():
    lt,rt=max(files),sum(files)
    res=1e9
    while lt<=rt:
        mid=(lt+rt)//2
        if check(mid):
            res=min(res,mid)
            rt=mid-1
        else: lt=mid+1
    return res

if __name__=="__main__":
    n,m=map(int,input().split())
    files=list(map(int,input().split()))
    print(solve())