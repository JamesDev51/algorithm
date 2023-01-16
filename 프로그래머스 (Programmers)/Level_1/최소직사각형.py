def solution(sizes):
    answer = 0
    largest=float('-inf')
    less_largest=float('-inf')
    for w,h in sizes:
        larger=max(w,h)
        smaller=min(w,h)
        largest=max(largest,larger)
        less_largest=max(less_largest,smaller)
    answer=largest*less_largest
    return answer