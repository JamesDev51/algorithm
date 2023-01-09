from math import comb

def solution(balls, share):
    answer = comb(balls,share)
    return answer