import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(n1,n2):
    now=n1
    if tree[n1]==n1 or tree[n2]==n2:return True
    while tree[now]!=now:
        if now==n2: return True
        now=tree[now]
    now=n2
    while tree[now]!=now:
        if now==n1: return True
        now=tree[now]
    return False

if __name__=="__main__":
    n=int(input())
    tree=dict()
    for _ in range(n-1):
        child,parents=input().split()
        if parents not in tree:tree[parents]=parents
        tree[child]=parents
    a,b=input().split()
    print(1 if check(a,b) else 0)

        
        