import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n=int(input())
    res=[]
    for i in range(1,n+1):
        res.append((i,1))
    for j in range(2,n):
        res.append((j,n))
        
    print(len(res))
    for q in res:print(*q)
    