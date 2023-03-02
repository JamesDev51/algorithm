import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solution(s,k):
    hash_lower=[0]*26
    hash_upper=[0]*26
    for ch in s:
        if ch.islower():hash_lower[ord(ch)-97]+=1
        if ch.isupper():hash_upper[ord(ch)-65]+=1
    ans=0
    for i in range(26):
        if hash_lower[i] +  hash_upper[i] >=2:
            if hash_lower[i]==hash_upper[i]:ans+=hash_lower[i];continue
            elif abs(hash_lower[i]-hash_upper[i])>=2 and k:
                mid=(hash_lower[i]+hash_upper[i])//2 #중간점
                need_op=min(abs(hash_lower[i]-mid),abs(hash_upper[i]-mid)) #필요한 op
                if need_op<=k:
                    ans+=mid
                    k-=need_op
                elif 0<k<need_op:
                    ans+=(min(hash_lower[i],hash_upper[i])+k)
                    k=0
                else:
                    ans+=min(hash_lower[i],hash_upper[i])
            else:
                    ans+=min(hash_lower[i],hash_upper[i])
    return ans    
    
if __name__=="__main__":
    for _ in range(int(input())):
        n,k=map(int,input().split())
        s=input().strip()
        print(solution(s,k))