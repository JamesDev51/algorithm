def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    prev=float('-inf')
    for s,e in routes:
        if s<=prev<=e:continue #가능
        else:
            prev=e
            answer+=1
    return answer