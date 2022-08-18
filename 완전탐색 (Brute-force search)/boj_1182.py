import sys
sys.stdin = open("input.text",  "rt")
import sys
from itertools import combinations
input=sys.stdin.readline


if __name__=="__main__":
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    res=0
    for i in range(1,n+1):
        for comb in combinations(arr,i):
            if sum(comb)==s:res+=1
    print(res)