import heapq

parents=list(range(100))
def find_parents(node):
    if parents[node]==node:return node
    parents[node]=find_parents(parents[node])
    return parents[node]

def union_parents(n1,n2):
    N1=find_parents(n1)
    N2=find_parents(n2)
    if N1<=N2:parents[N2]=N1
    else:parents[N1]=N2
def is_parents_equal(n1,n2):
    return find_parents(n1)==find_parents(n2)
    
def solution(n, costs):
    answer = 0
    heap=[]
    for n1,n2,cost in costs:
        heapq.heappush(heap,(cost,n1,n2))
    while heap:
        cost,n1,n2=heapq.heappop(heap)
        if not is_parents_equal(n1,n2):
            union_parents(n1,n2)
            answer+=cost
        
        
    return answer