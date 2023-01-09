from itertools import permutations

def solution(spell, dic):
    answer = 2
    for perm in permutations(spell,len(spell)):
        if ''.join(perm) in dic:return 1
    return answer