import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        plus=dict()
        minus=dict()
        
        for num in arr:
            if num>0:
                plus[num]=1
            else:
                minus[abs(num)]=1
        
        pair_cnt=0
        for key in plus.keys():
            if key in minus:
                pair_cnt+=1
        plus_size=len(plus)
        minus_size=len(minus)
        for i in range(1,plus_size+1):
            print(i,end=" ")
        for j in range(i-1,i-minus_size-1,-1):
            print(j,end=" ")
        print()
        for i in range(pair_cnt):
            print("1 0",end=" ")
        for j in range(1,plus_size-pair_cnt+1):
            print(j,end=" ")      
        print()