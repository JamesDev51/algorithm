import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(current):
    global cnt,current_sum
    if current==n: return
    if current_sum+arr[current]==s: cnt+=1

    dfs(current+1) #이번 원소를 포함 시키지 않음

    current_sum+=arr[current] #이번 원소를 포함
    dfs(current+1)

    current_sum-=arr[current]
    
if __name__=="__main__":
    n,s=map(int, input().split())
    arr=list(map(int, input().split()))
    cnt,current_sum=0,0
    dfs(0)
    print(cnt)
    