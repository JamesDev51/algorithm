import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n=int(input())
    ans=0
    acc=1;e=1
    while acc<n:
        acc+=(6*e)
        e+=1
    print(e)