import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from math import sqrt


if __name__=="__main__":
    a,b=map(int,input().split())
    a*=2
    if sqrt(pow(a,2)-4*b)==0:
        print(int(-a)//2)
    else:
        print(int(-a-sqrt(pow(a,2)-4*b))//2,int(-a+sqrt(pow(a,2)-4*b))//2)
        