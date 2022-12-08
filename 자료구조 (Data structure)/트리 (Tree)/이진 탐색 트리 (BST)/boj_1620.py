import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,m=map(int,input().split())
    nameNum=dict()
    numName=dict()
    for num in range(1,n+1):
        name=input().strip()
        nameNum[name]=num
        numName[num]=name
    for _ in range(m):
        a=input().strip()
        if a.isdigit():print(numName[int(a)])
        else: print(nameNum[a])

        