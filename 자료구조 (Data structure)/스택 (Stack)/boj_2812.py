import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,k=map(int,input().split())
    num_list=list(map(int,list(input())))
    stack=[]
    for num in num_list:
        while stack and stack[-1]<num and k:
            k-=1
            stack.pop()
        stack.append(num)
    while k:
        k-=1
        stack.pop()
    print(''.join(map(str,stack)))