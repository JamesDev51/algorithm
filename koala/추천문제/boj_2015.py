import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    ch=dict()
    acc=0
    cnt=0
    for i in range(n):
        num=acc+arr[i]
        gap=abs(k-num)
        if gap in ch:
            cnt+=ch[gap]
        
        print(num,gap,ch)
        
        if num in ch:ch[num]+=1
        else:ch[num]=1
        acc=num
    print(cnt)