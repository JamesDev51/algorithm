import random

def merge_lists(A,B):
    if not A: return B  #A가 비었으면  B 리턴
    if not B: return A  #B가 비었으면 A 리턴

    #가장 작은 원소만 빼고 재귀적으로 다시 병합
    if A[0] < B[0]: return [A[0]] + merge_lists(A[1:], B) 
    else: return [B[0]]+merge_lists(A, B[1:]) 
    
def merge_sort(A):
    if len(A)==1: return A
    return merge_lists(merge_sort(A[:len(A)//2]), merge_sort(A[len(A)//2:])) #절 반씩 쪼개가면서 병합 시킴


if __name__=="__main__":
    num_list=list(range(1,21))
    random.shuffle(num_list)
    print("정렬 전 :",num_list)
    print("정렬 후 :",merge_sort(num_list))