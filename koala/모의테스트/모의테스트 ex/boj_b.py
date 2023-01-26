import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init():
    global lt,rt
    ch[c]=1
    for i in range(lt,rt+1):
        dish=dishes[i]
        if  dish not in ch: ch[dish]=1
        else: ch[dish]+=1
    rt+=1

def solve():
    global largest, lt ,rt
    diverse=len(ch)
    while rt<len(dishes):
        tail_dish=dishes[lt]
        if ch[tail_dish]-1==0: diverse-=1
        ch[tail_dish]-=1; lt+=1
        
        head_dish=dishes[rt]
        if head_dish not in ch or ch[head_dish]+1==1: ch[head_dish]=0;diverse+=1
        ch[head_dish]+=1; rt+=1
        largest=max(largest,diverse)
    

if __name__=="__main__":
    n,d,k,c=map(int,input().split())
    dishes=[int(input()) for _ in range(n)]
    dishes=dishes+dishes[:k-1]
    lt,rt=0,k-1
    ch=dict()
    init()
    largest=len(ch)
    solve()
    print(largest)
    
    