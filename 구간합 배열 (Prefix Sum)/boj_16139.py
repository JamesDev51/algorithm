import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    s=input().strip()
    p_sum=[[0]*len(s) for _ in range(26)]
    for i in range(len(s)):
        if i!=0:
            for j in range(26):
                p_sum[j][i]+=p_sum[j][i-1]
        p_sum[ord(s[i])-97][i]+=1
    
    for _ in range(int(input())):
        a,l,r=input().split()
        l,r=int(l),int(r)
        print(p_sum[ord(a)-97][r]-(p_sum[ord(a)-97][l-1] if 0<=l-1 else 0)  )