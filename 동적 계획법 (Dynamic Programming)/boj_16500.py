import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(idx):
    global result
    if idx==len(s):result=1;return
    if dp[idx]: return
    dp[idx]=1
    for word in words:
        if len(s[idx:])>=len(word):
            for i in range(len(word)):
                if word[i]!=s[idx+i]:break
            else:solve(idx+len(word))
        
if __name__=="__main__":
    s=input().strip()
    n=int(input())
    dp=[0]*101
    words=list(input().strip() for _ in range(n))
    result=0
    solve(0)
    print(result)