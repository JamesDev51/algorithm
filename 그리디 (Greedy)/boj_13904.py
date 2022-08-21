import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    score=[0]*1001
    for i in range(n):
        d,w=info[i]
        for j in range(d,0,-1):
            if not score[j]:
                score[j]=w
                break
    print(sum(score))

if __name__=="__main__":
    n=int(input())
    info=[list(map(int,input().split())) for _ in range(n)]
    info.sort(key=lambda x:(-x[1],x[0]))
    solve()