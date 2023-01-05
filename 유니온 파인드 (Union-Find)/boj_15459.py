import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def check(idx,flavor, spicy):
    lt,rt=idx-1,idx+1
    totalFlavor=flavor
    
    while 0<=lt or rt<n:
        flag=False
        if 0<=lt and haybales[lt][1]<=spicy:totalFlavor+=haybales[lt][0];lt-=1;flag=True
        if rt<n and haybales[rt][1]<=spicy:totalFlavor+=haybales[rt][0];rt+=1; flag=True
        if m<=totalFlavor:return True
        if not flag: return False
    return False

            
def solve():
    for i in range(n):
        idx,f,s=cpHaybales[i]
        if check(idx,f,s): return s



if __name__=="__main__":
    n,m=map(int,input().split())
    haybales=[list(map(int,input().split())) for _ in range(n)]
    cpHaybales=[]
    for idx,data in enumerate(haybales):
        f,s=data
        cpHaybales.append((idx,f,s))
    cpHaybales.sort(key=lambda x : x[2])
    
    print(solve())