import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    lt,rt=0,m
    cnt=0
    sub_sum=sum(money[lt:rt])
    if sub_sum<k:cnt+=1
    while rt<len(money):
        sub_sum-=money[lt];lt+=1
        sub_sum+=money[rt];rt+=1
        if sub_sum<k:cnt+=1
    return cnt
    

if __name__=="__main__":
    for _ in range(int(input())):
        n,m,k=map(int,input().split())
        money=list(map(int,input().split()))
        if n!=m: money=money+money[:m-1]
        print(solve())