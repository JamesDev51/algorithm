import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    stack=[]
    answer=[0]*n
    for i in range(n):
        num=a[i]
        while stack and stack[-1][0]<num:
            p_num,p_i=stack.pop()
            answer[p_i]=num
        stack.append((num,i))
    while stack:
        p_num,p_i=stack.pop()
        answer[p_i]=-1
    print(*answer)        