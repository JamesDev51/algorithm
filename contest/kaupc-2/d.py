import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    res=float('inf')
    lt,rt=0,k
    while rt<n:
        res=min(res,max(costs[lt],costs[rt]))
        lt+=1;rt+=1
    return res
        
        
if __name__=="__main__":
    n,k=map(int,input().split())
    costs=list(map(int,input().split()))
    print(solve())