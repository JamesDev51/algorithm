import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dp(last,used,pos):
    if pos==n:
        return 1 if used==((1<<10)-1) else 0
    
    ret=0
    if last==0: ret+=dp(1,used&1<<1,pos+1)%mod
    elif last==9: ret+=dp(8,used&1<<8,pos+1)%mod
    else: 
        ret+=dp(last-1,used&1<<(last-1),pos+1)%mod
        ret+=dp(last+1,used&1<<(last+1),pos+1)%mod
    return ret%mod
    


if __name__=="__main__":
    mod=1000000000
    n=int(input())
    
    res=0
    for start in range(1,10):
        res+= dp(start,1<<start,1)%mod
    print(res%mod)