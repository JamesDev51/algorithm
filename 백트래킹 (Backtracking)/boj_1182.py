import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def dfs(arr,n,s,idx,sub_sum,cnt):
    ret=0
    if idx==n:
        if sub_sum==s and cnt>0: ret+=1
    else:
        ret+=dfs(arr, n, s, idx+1,sub_sum+arr[idx],cnt+1)
        ret+=dfs(arr, n, s, idx+1,sub_sum,cnt)
    return ret
    

def solution(arr,n,s):
    answer=0
    answer+=dfs(arr,n,s,0,0,0)
    return answer

if __name__=="__main__":
    n,s=map(int, input().split())
    arr=list(map(int, input().split()))
    print(solution(arr,n,s))