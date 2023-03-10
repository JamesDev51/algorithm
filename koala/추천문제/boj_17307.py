import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,c=map(int,input().split())
    arr=list(map(int,input().split()))
    res_idx=0; smallest=float('inf')
    
    right_acc=[0]*n
    left_acc=[0]*n
    for i in range(n-1):
        now,right=arr[i],arr[i+1]
        if now>right:right_acc[i+1]=right_acc[i]+(c-now+right)
        else:right_acc[i+1]=right_acc[i]+(right-now)
    for i in range(n-1,0,-1):
        now,left=arr[i],arr[i-1]
        if now>left:left_acc[i-1]=left_acc[i]+(c-now+left)
        else:left_acc[i-1]=left_acc[i]+(left-now)
    for i in range(n):
        if i==0:
            largest=right_acc[-1]-right_acc[i]
        elif i==n-1:
            largest=left_acc[0]-left_acc[i]
        else:
            largest=max(right_acc[-1]-right_acc[i],left_acc[0]-left_acc[i])
        if largest<smallest:
            smallest=largest
            res_idx=i+1
    print(res_idx)
    print(smallest)