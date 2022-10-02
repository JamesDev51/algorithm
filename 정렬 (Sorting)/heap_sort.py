import random
import heapq

def heap_sort(A):
    heapq.heapify(A) #A를 힙으로 만듬
    result=[]
    
    while A:
        root_num=heapq.heappop(A)
        result.append(root_num)
    return result

if __name__=="__main__":
    num_list=list(range(1,21))
    random.shuffle(num_list)
    print("정렬 전 :",num_list)
    print("정렬 후 :",heap_sort(num_list))