import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


if __name__=="__main__":
    res=0
    n,k=map(int,input().split())
    ques=[deque() for _ in range(21)]
    for idx in range(n):
        word=input().strip()
        while ques[len(word)] and idx-ques[len(word)][0]>k:
            ques[len(word)].popleft()
        res+=len(ques[len(word)])
        ques[len(word)].append(idx)
    print(res)
        