import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

MOD=1000000000000007
def mod(n):
    if n>=0: return n%MOD
    else: return ((-n//MOD+1)*MOD+n)%MOD
    
if __name__=="__main__":
    t=input().rstrip()
    p=input().rstrip()
    n,m=len(t),len(p)
    
    res=[]
    g,h=0,0
    power=1
    for i in range(n-m+1):
        if i==0: #가장 처음 해시값을 계산
            for j in range(m):
                g=mod(g+ord(t[m-1-j])*power)
                h=mod(h+ord(p[m-1-j])*power)
                if j<m-1: power=mod(power*7)  #가장 큰 값으로 그대로 유지 (이 부분을 빼줘야 하니까)
        else: g = mod(7*(g-ord(t[i-1])*power) + ord(t[i+m-1]))
        if g==h:
            res.append(i+1)
    print(len(res))
    print(*res)
    