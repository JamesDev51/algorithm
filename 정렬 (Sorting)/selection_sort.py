import random

def selection_sort(A):
    for i in range(len(A)-1):
        index_min=i #위치를 선택해준다.
        for j in range(i,len(A)):
            if A[j]<A[index_min]: #선택된 위치보다 작은 값의 인덱스를 저장한다.
                index_min=j
        A[i],A[index_min]=A[index_min],A[i] #순회가 끝나면 선택한 위치와 순회에서 가장 작은 값을 교환한다.
    return A

if __name__=="__main__":
    num_list=list(range(1,21))
    random.shuffle(num_list)
    print("정렬 전 :",num_list)
    print("정렬 후 :", selection_sort(num_list))