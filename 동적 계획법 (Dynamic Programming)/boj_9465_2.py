import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():

    for y in range(2):
        for x in range(n):
            res=max(res,dp[y][x]) 
    return res

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        mat=[list(map(int,input().split())) for _ in range(2)]
        print(solve())