import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    answer=0
    lt,rt=0,n-1
    while lt<=rt:
        answer=max(answer,(rt-lt-1)*min(arr[lt],arr[rt]))
        if arr[lt]<arr[rt]: lt+=1
        else:rt-=1
        
    return answer

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(solve())