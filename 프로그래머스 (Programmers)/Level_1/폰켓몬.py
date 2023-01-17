def solution(nums):
    answer = 0
    size=len(nums)
    nums_set=set(nums)
    answer=min(size//2,len(nums_set))
    return answer