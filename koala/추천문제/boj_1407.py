import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solution():
    ret=0
    if a%2==0 and b%2==0:ret+=(b-a)//2
    else:ret+=((b-a)//2+1)
    i=1
    while pow(2,i)<=b:
        exp=pow(2,i)
        lt,rt=a//exp,b//exp
        while lt%2==0 or exp*lt<a:lt+=1
        while rt%2==0 or b<exp*rt:rt-=1
        i+=1
        if not a<=exp*lt<=b and not a<=exp*rt<=b:continue
        gap=(rt-lt)
        ret+=(gap//2+1)*exp
        
        
    return ret

if __name__=="__main__":
    a,b=map(int,input().split())
    print(solution())
    