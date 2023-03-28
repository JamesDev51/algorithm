import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    ropes=[int(input()) for _ in range(int(input()))]
    ropes.sort()
    res=float('-inf')
    for i in range(len(ropes)):res=max(res,ropes[i]*(len(ropes)-i))
    print(res)