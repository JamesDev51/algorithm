def solution(array):
    answer = 0
    for num in array:
        answer+=str(num).count("7")
    return answer