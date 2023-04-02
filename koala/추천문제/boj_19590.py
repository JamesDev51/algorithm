import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq


if __name__=="__main__":
    n=int(input())
    arr=[int(input()) for _ in range(n)]
    arr.sort()
    largest=arr[-1]
    sub_sum=sum(arr[:-1])
    if largest>sub_sum:print(largest-sub_sum)
    else:
        if sum(arr)%2==0:print(0)
        else:print(1)