import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        p_sum=[0]*(n+1)
        for i in range(1,n+1): p_sum[i]=p_sum[i-1]+arr[i-1]
        
        print(p_sum)
        largest=float('-inf')
        for i in range(1,n+1):
            for j in range(i,n+1):
                largest=max(largest, p_sum[j]-p_sum[j-i])
        print(largest)
        
        
        