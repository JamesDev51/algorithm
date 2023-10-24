import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    m,n=map(int,input().split())
    max_plus=[[0]*m for _ in range(m)]
    mat=[[1]*m for _ in range(m)]
    
    acc=[0]*(2*m-1)
    for _ in range(n):
        z,o,t=map(int,input().split())
        idx=z
        if o>0:
            acc[idx]+=1
            idx+=o
        if t>0:
            if o>0:
                acc[idx]-=1
            acc[idx]+=2
    for i in range(1,2*m-1):
        acc[i]+=acc[i-1]
    idx=0
    for y in range(m-1,-1,-1):
        max_plus[y][0]+=acc[idx];idx+=1
    for x in range(1,m):
        max_plus[0][x]+=acc[idx];idx+=1
    for y in range(1,m):
        for x in range(1,m):
            max_plus[y][x]=max(max_plus[y-1][x],max_plus[y-1][x-1],max_plus[y][x-1])
    for y in range(m):
        for x in range(m):
            print(max_plus[y][x]+1,end=" ")
        print()

        