import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n,k=map(int,input().split())
    books=[[] for _ in range(11)]
    cnt=0
    for _ in range(n):
        c,g=map(int,input().split())
        books[g].append(c)
    for i in range(11):
        books[i].sort(reverse=True)
        if len(books[i])==0:continue
        for j in range(1,len(books[i])):
            books[i][j]=(books[i][j] if j else 0)+books[i][j-1] #누적합
    dp=[0]*(k+1)
    for i in range(1,11):
        for base in range(k,-1,-1): #지금까지 몇 권을 골랐는가
            for j in range(1,len(books[i])+1):
                if base+j>k:break
                dp[base+j]=max(dp[base+j],dp[base]+books[i][j-1]+(j-1)*j)
    print(dp[-1])