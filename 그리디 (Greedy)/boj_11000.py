import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    cnt=0; 

if __name__=="__main__":
    n=int(input())
    info=[list(map(int,input().split())) for _ in range(n)]
    info.sort(key=lambda x:(x[1],x[0]))
    print(solve())