def solution(arr, divisor):
    answer = []
    for element in arr:
        if element%divisor==0: answer.append(element)
    answer.sort()
    return answer if answer else [-1]