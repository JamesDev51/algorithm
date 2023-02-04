import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    lt,rt=0,0
    sub_sum=0
    answer=float('inf')
    flag=True
    while lt<=rt and flag:
        flag=False
        if sub_sum<s and  rt<n:
            sub_sum+=arr[rt]
            flag=True
            rt+=1
        elif sub_sum>=s and lt<n:
            answer=min(answer,(rt-lt))
            flag=True
            sub_sum-=arr[lt] 
            lt+=1
    print(answer if answer!=float('inf') else 0)
        
        