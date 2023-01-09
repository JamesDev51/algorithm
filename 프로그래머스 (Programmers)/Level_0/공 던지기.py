def solution(numbers, k):
    answer = numbers.index(1)
    l=len(numbers)
    for _ in range(k-1):
        answer+=2
        answer%=l
    answer=numbers[answer]
    return answer