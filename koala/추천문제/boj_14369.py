import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

from copy import deepcopy

a=dict()
a[0]='ZERO'
a[1]='ONE'
a[2]='TWO'
a[3]='THREE'
a[4]='FOUR'
a[5]='FIVE'
a[6]='SIX'
a[7]='SEVEN'
a[8]='EIGHT'
a[9]='NINE'
c=[[0]*26 for _ in range(10)]
for i in range(10):
    for ch in a[i]:
        c[i][ord(ch)-65]+=1
        
def go(num,b,res):
    global ans
    if sum(b)==0:
        ans=res
        return
    if num==10:return
    cnt=float('inf')
    for i in range(26):
        if c[num][i]==0:continue
        cnt=min(cnt,b[i]//c[num][i])
        
    if cnt in [0,float('inf')]:go(num+1,b,res)
    else:
        for j in range(cnt+1):
            cp_b=deepcopy(b)
            for i in range(26):
                if c[num][i]==0:continue
                cp_b[i]-=j*c[num][i]

            go(num+1,cp_b,res+str(num)*j)
            

if __name__=="__main__":
    for t in range(1,int(input())+1):
        s=input().strip()
        
        b=[0]*26
        for ch in s:
            b[ord(ch)-65]+=1
            
        ans=""
        go(0,b,"")
        print(f"Case #{t}: {ans}")