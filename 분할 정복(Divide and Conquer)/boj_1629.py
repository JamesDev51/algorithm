import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def divide(e):
    global a,c
    if e==1: return a%c
    if e%2==0: #짝수
        return (divide(e//2)**2)%c
    else: #홀수
        return ((divide(e//2)**2)%c*a)%c
    

if __name__=="__main__":
    a,b,c=map(int,input().split())
    print(divide(b))