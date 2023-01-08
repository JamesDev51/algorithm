def solution(my_string):
    answer = list(my_string.lower())
    answer.sort()
    return ''.join(answer)