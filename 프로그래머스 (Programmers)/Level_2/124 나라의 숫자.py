def solution(n):
    answer = ''
    while n:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer