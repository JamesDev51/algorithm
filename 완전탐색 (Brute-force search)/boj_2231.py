import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def get_number_sum(num):
    sum=0
    while num:
        sum+=(num%10)
        num//=10
    return sum
if __name__=="__main__":
    n=int(input())
    for num in range(1,10**6+1):
        if num+get_number_sum(num)==n:print(num);exit(0)
    print(0)
        
