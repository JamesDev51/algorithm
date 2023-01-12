def solution(a, b):
    answer = sum([i for i in range(a,b+1)]) if a<=b else sum([i for i in range(b,a+1)])
    return answer