import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    towers=list(map(int,input().split()))
    stack=[]
    answer=[0]*n
    for i in range(n,0,-1):
        tower=towers[i-1]
        while stack and stack[-1][0]<tower:
            _,p_i=stack.pop()
            answer[p_i-1]=i
        stack.append((tower,i))
    while stack:
        _,p_i=stack.pop()
        answer[p_i-1]=0
    print(*answer)
    