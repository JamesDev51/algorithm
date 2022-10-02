import random

def bubble_sort(A):
    for i in range(len(A)-1): #base는 마지막 하나 전까지
        for j in range(len(A)-1-i): #i를 빼주는 이유는 뒷쪽은 이미 오름차순으로 정렬된 상태이기 때문
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]
    return A

if __name__=="__main__":
    num_list=list(range(1,21))
    random.shuffle(num_list)
    print("정렬 전 :",num_list)
    print("정렬 후 :", bubble_sort(num_list))