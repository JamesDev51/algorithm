import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def manhathan(c1,c2):
    return abs(c1[0]-c2[0])+abs(c1[1]-c2[1])

if __name__=="__main__":
    n=int(input())
    coords=list(list(map(int,input().split())) for _ in range(n))
    acc=[0]+[manhathan(coords[i],coords[i-1]) for i in range(1,n)]
    for i in range(1,n):acc[i]+=acc[i-1]        
    answer=float('inf')
    for i in range(1,n-1):
        answer=min(answer,acc[i-1]-acc[0]+acc[n-1]-acc[i+1]+manhathan(coords[i-1],coords[i+1]))
    print(answer)
        
        