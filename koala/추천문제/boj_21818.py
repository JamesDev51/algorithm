import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from itertools import combinations_with_replacement as cwr

def check(tmp,arr):
    for num in arr:
        if num not in tmp:return False
    return True

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        abc=set(arr)
        for num1 in arr:
            for num2 in arr:
                if num1-num2>0:abc.add(num1-num2)
        cnt=0
        for comb in cwr(abc,3):
            tmp=list(comb)
            tmp.append(comb[0]+comb[1])
            tmp.append(comb[1]+comb[2])
            tmp.append(comb[0]+comb[2])
            tmp.append(sum(comb))
            if check(tmp,arr):cnt+=1 
        print(cnt)