def solution(i, j, k):
    answer = 0
    str_k=str(k)
    for num in range(i,j+1):
        answer+=(str(num).count(str_k))
    return answer