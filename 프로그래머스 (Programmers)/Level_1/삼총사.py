from itertools import combinations

def solution(number):
    answer = 0
    for com in combinations(number,3):
        if sum(com)==0:answer+=1
    
    return answer