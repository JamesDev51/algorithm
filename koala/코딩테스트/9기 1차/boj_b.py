import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n,d=map(int,input().split())
    answer=0
    for num in range(1,n+1):
        answer+= str(num).count(str(d))
    print(answer)