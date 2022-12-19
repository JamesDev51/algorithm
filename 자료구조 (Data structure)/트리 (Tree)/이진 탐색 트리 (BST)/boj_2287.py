import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def monodigital():
    dp=[set() for _ in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(k)*i))
        for j in range(1,i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1+num2)
                    dp[i].add(num1-num2)
                    if num2!=0: dp[i].add(num1//num2)
                    dp[i].add(num1*num2)
        if a in dp[i]: return i
    return "NO"
    
if __name__=="__main__":
    k=int(input())
    n=int(input())
    for _ in range(n):
        a=int(input())
        print(monodigital())
        