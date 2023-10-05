import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    buildings=list(int(input()) for _ in range(n))
    stack=[]
    answer=[0]*n
    for i in range(n-1,-1,-1):
        building=buildings[i]
        possible_sum=0
        while stack and stack[-1][0]<building:
            p_building,p_cnt=stack.pop()
            possible_sum+=(p_cnt+1)
        answer[i]=possible_sum
        stack.append((building,possible_sum))
    print(sum(answer))