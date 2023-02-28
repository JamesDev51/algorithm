import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq

if __name__=="__main__":
    for _ in range(int(input())):
        num_hash=dict()
        max_heap=list();min_heap=list()
        for _ in range(int(input())):
            command,num=input().split(" ")
            num=int(num)
            if command=="I":
                if num in num_hash:num_hash[num]+=1
                else:num_hash[num]=1
                heapq.heappush(max_heap,-num)
                heapq.heappush(min_heap,num)
            else:
                if num==1:
                    while max_heap:
                        poped=-heapq.heappop(max_heap)
                        if num_hash[poped]==0:continue
                        else:num_hash[poped]-=1;break
                            
                else:
                    while min_heap:
                        poped=heapq.heappop(min_heap)
                        if num_hash[poped]==0:continue
                        else:num_hash[poped]-=1;break
        largest,smallest=float('-inf'),float('inf')
        while max_heap:
            poped=-heapq.heappop(max_heap)
            if num_hash[poped]==0:continue
            else:largest=poped;break
        while min_heap:
            poped=heapq.heappop(min_heap)
            if num_hash[poped]==0:continue
            else:smallest=poped;break
        if largest==float('-inf') and smallest==float('inf'):print("EMPTY")
        else: print(largest,smallest)