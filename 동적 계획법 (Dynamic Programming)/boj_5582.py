import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    s1=input().strip()
    s2=input().strip()
    dp=[[0]*(len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1]==s1[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
    res=float('-inf')
    for q in dp:res=max(res,max(q))
    print(res)