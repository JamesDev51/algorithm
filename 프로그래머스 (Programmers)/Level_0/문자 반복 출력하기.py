def solution(my_string, n):
    answer = ''
    for st in my_string:
        answer+=(n*st)
    return answer