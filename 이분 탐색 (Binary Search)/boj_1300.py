import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(limit):
    sum=0
    for i in range(1,n+1):sum+=min(limit//i,n)
    
    return sum
def solve():
    lt,rt=1,n**2
    res=float('inf')
    while lt<=rt:
        mid=(lt+rt)//2
        cnt=check(mid)
        if k<=cnt:
            res=min(res,mid)
            rt=mid-1
        else:lt=mid+1
    return res

if __name__=="__main__":
    n=int(input())
    k=int(input())
    print(solve())