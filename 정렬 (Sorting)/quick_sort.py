import random

def quick_sort(A):
    if len(A)<=1: return A #길이가 0이거나 1인 경우는 이미 정렬된 경우
    
    pivot=len(A)//2 #피벗 중간으로 잡음
    left,right=[],[]
    
    for num in A[:pivot]+A[pivot+1:]:
        if num<A[pivot]:left.append(num) #작으면 왼쪽
        else: right.append(num) #크거나 같으면 오른쪽
        
    return quick_sort(left) + [A[pivot]] + quick_sort(right) #pivot 기준으로 작은, 크거나 같은 두개로 분리된 리스트를 재귀적으로 정렬 후 합침

if __name__=="__main__":
    num_list=list(range(1,21))
    random.shuffle(num_list)
    print("정렬 전 :",num_list)
    print("정렬 후 :",quick_sort(num_list))