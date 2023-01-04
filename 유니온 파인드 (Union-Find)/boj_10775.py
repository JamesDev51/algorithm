import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

def getParents(node):
    if node==parents[node] or not used[node]:
        return node
    parents[node] = getParents(parents[node])
    return parents[node]

def union(n1,n2):
    N1=getParents(n1)
    N2=getParents(n2)
    if N1<N2:parents[N2]=N1
    elif N1>N2: parents[N1]=N2
    else:return

def landing(gate):
    if not used[gate]:
        used[gate]=1
        return True
    pGate=getParents(gate) #앞에서 가장 가까운 비어있는 곳
    if not used[pGate]: #사용 안하는 중이면
        used[pGate]=1 #넣고
        union(gate,pGate) #새로 가까운 곳
        return True
    else: return False

if __name__=="__main__":
    g=int(input())
    parents=list(range(g+1))
    used=[0]*(g+1)
    for i in range(2,g+1):
        parents[i]=i-1
    p=int(input())
    answer=0
    for _ in range(p):
        gComing=int(input())
        if landing(gComing):answer+=1
        else:break
    print(answer)