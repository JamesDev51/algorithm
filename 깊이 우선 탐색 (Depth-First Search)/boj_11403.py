import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    for start in range(n):
        ch=[0]*n
        for end in range(n):
            if mat[start][end]:
                stack.append(end)
                res[start][end]=1
                ch[end]=1
        while stack:
            node=stack.pop()
            for next_node in range(n):
                if mat[node][next_node] and not ch[next_node]:
                    ch[next_node]=1
                    res[start][next_node]=1
                    stack.append(next_node)     
if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    res=[[0]*n for _ in range(n)]
    stack=[]
    solve()
    for row in res:print(*row)