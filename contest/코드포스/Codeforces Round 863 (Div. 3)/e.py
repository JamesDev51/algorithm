import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(num):
    a="012356789"
    res=""
    while num:
        mod=num%9
        res+=a[mod]
        num=num//9
    return res[::-1]
        
if __name__=="__main__":
    for _ in range(int(input())):
        k=int(input())
        print(solve(k))
            
            
        