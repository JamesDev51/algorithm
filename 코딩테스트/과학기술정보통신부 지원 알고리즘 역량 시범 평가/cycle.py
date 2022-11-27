import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    tree=[[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    
