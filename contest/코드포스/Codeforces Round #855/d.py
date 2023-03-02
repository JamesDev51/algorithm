import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        s=input().strip()
        ans=n-1
        for i in range(n-2):
            if s[i]==s[i+2]:ans-=1
        print(ans)