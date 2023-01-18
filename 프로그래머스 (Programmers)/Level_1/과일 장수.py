def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    start_idx=0
    while len(score)-start_idx>=m:
        minimum=min(score[start_idx:start_idx+m])
        answer+=(minimum*m)            
        start_idx+=m
    return answer