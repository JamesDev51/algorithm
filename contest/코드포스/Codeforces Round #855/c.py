import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline


if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        cards=list(map(int,input().split()))
        ans=0
        heap=[]
        for i in range(n):
            card=cards[i]
            if card==0:
                if heap:ans+=(-heapq.heappop(heap))
            else:
                heapq.heappush(heap,-card)
        print(ans)
                
                
            
            