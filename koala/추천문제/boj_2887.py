import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def find_parents(node):
    if node==parents[node]:return node
    parents[node]=find_parents(parents[node])
    return parents[node]
def union_parents(n1,n2):
    N1=find_parents(n1)
    N2=find_parents(n2)
    if N1<=N2:parents[N2]=N1
    else:parents[N1]=N2
def is_same_parents(n1,n2):
    return find_parents(n1)==find_parents(n2)

if __name__=="__main__":
    n=int(input())
    __a,__b,__c=[],[],[]
    for i in range(n):
        a,b,c=map(int,input().split())
        __a.append((a,i))
        __b.append((b,i))
        __c.append((c,i))
    __a.sort(reverse=True);__b.sort(reverse=True);__c.sort(reverse=True)
    _a,_b,_c=[],[],[]
    for i in range(n-1):
        _a.append((__a[i][0]-__a[i+1][0],__a[i][1],__a[i+1][1]))
        _b.append((__b[i][0]-__b[i+1][0],__b[i][1],__b[i+1][1]))
        _c.append((__c[i][0]-__c[i+1][0],__c[i][1],__c[i+1][1]))
    _a.sort();_b.sort();_c.sort()
    res=0
    parents=list(range(n))
    ai,bi,ci=0,0,0
    while True:
        while ai<n-1 and is_same_parents(_a[ai][1], _a[ai][2]):ai+=1
        while bi<n-1 and is_same_parents(_b[bi][1], _b[bi][2]):bi+=1
        while ci<n-1 and is_same_parents(_c[ci][1], _c[ci][2]):ci+=1
        a_gap=_a[ai][0] if ai<n-1 and not is_same_parents(_a[ai][1], _a[ai][2]) else float('inf')
        b_gap=_b[bi][0] if bi<n-1 and not is_same_parents(_b[bi][1], _b[bi][2]) else float('inf')
        c_gap=_c[ci][0] if ci<n-1 and not is_same_parents(_c[ci][1], _c[ci][2]) else float('inf')
        smallest=min(a_gap,b_gap,c_gap)
        if smallest==float('inf'):break
        elif smallest==a_gap:
            union_parents(_a[ai][1], _a[ai][2])
        elif smallest==b_gap:
            union_parents(_b[bi][1], _b[bi][2])
        else:
            union_parents(_c[ci][1], _c[ci][2])
        res+=smallest
    print(res)