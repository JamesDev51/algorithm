from itertools import combinations

def solution(numbers):
    answer = set()
    for comb in combinations(numbers,2):
        answer.add(sum(comb))
    answer=list(answer)
    answer.sort()
    
    return answer