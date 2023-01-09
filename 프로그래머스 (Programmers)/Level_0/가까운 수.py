from bisect import bisect_left

def solution(array, n):
    array.sort()
    idx=bisect_left(array,n)
    print(idx)
    if idx==0:
        answer=array[0]
    elif idx==len(array):
        answer=array[-1]
    else:
        answer=array[idx-1] if n-array[idx-1]<=array[idx]-n else array[idx]
    return answer
        