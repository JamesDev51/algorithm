from itertools import combinations

def solution(numbers):
    answer = float('-inf')
    for comb in combinations(numbers,2):
        answer=max(answer,comb[0]*comb[1])
    return answer