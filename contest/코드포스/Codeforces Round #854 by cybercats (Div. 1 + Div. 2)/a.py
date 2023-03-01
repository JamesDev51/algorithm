import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().split())
        nums=list(map(int,input().split()))
        res=[-1]*(n+1)
        used=set() 
        pop_turn=n
        for i in range(len(nums)):
            num=nums[i]
            if num in used:
                continue
            else:
                res[pop_turn]=(i+1)
                used.add(num)
                pop_turn-=1
            if pop_turn==0:break

        print(*res[1:])