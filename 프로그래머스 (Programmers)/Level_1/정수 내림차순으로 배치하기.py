def solution(n):
    answer = int(''.join(list(sorted(list(str(n)),reverse=True))))
    return answer