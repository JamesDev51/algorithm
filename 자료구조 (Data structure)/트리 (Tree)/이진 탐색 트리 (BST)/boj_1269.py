import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    na,nb=map(int,input().split())
    a=set(map(int,input().split()))
    b=set(map(int,input().split()))
    print(len(a.symmetric_difference(b)))