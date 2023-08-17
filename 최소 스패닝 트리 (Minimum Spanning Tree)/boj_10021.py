import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline

def find_parents(node):
    if parents[node]!=node:
        parents[node]=find_parents(parents[node])
    return parents[node]

def union_parents(n1,n2):
    N1=find_parents(n1)
    N2=find_parents(n2)
    if N1<=N2:parents[N2]=N1
    else:parents[N1]=N2
    
def is_parents_equal(n1,n2):
    return find_parents(n1)==find_parents(n2)

def solve():
    global n
    answer=0
    cnt=1
    while heap:
        dist,i,j=heapq.heappop(heap)
        if not is_parents_equal(i,j):
            union_parents(i,j)
            answer+=dist
            cnt+=1
        if cnt==n:return answer
    return answer if cnt==n else -1
        
if __name__=="__main__":
    n,c=map(int,input().split())
    coords=list(tuple(map(int,input().split())) for _ in range(n))
    heap=[]
    parents=list(range(n))
    for i in range(n):
        xi,yi=coords[i]
        for j in range(i+1,n):
            xj,yj=coords[j]
            dist=pow(xi-xj,2)+pow(yi-yj,2)
            if c<=dist:heapq.heappush(heap,(dist,i,j))
    print(solve())