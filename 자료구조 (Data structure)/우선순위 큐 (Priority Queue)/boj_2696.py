import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline


if __name__=="__main__":
    for _ in range(int(input())):
        m=int(input())
        res=[]
        leftHeap,rightHeap=[],[]
        middlePosition=0 #0이면 left, 1이면 right
        idx=1
        middle=float('inf')
        for row in range((m//10)+1):
            nums=list(map(int,input().split()))
            for num in nums:
                if num<=middle: heapq.heappush(leftHeap,-num)
                else: heapq.heappush(rightHeap,num)
                
                if len(leftHeap)+1==len(rightHeap): heapq.heappush(leftHeap,-heapq.heappop(rightHeap))
                elif len(leftHeap)>len(rightHeap)+1: heapq.heappush(rightHeap,-heapq.heappop(leftHeap))
                
                if idx%2==1:#중앙값 갱신
                    middle=-leftHeap[0]
                    res.append(middle)
                idx+=1
            
        print(len(res))
        for row in range(len(res)//10+1):
            print(*res[10*row:10*(row+1)])    
            