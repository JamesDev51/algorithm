import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(start,end):
    if start==end: return [arr[start]] 
    mid=(start+end)//2
    
    left=solve(start,mid)
    right=solve(mid+1,end)
    lt,rt=0,0
    new_arr=[]
    while lt<len(left) and rt<len(right):
        if left[lt]<=right[rt]:new_arr.append(left[lt]); lt+=1
        else: new_arr.append(right[rt]);rt+=1
    while lt<len(left):new_arr.append(left[lt]);lt+=1
    while rt<len(right): new_arr.append(right[rt]);rt+=1
    
    if (end-start+1)==n/k:
        for i in range(start,end+1):answer[i]=new_arr[i-start]
    return new_arr
    

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    answer=[0]*n
    solve(0,n-1)
    print(*answer)