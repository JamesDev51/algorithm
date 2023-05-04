def solution(targets):
    targets.sort(key=lambda x:x[1])
    answer = 0
    lim=-1
    for i in range(len(targets)):
        if lim<=targets[i][0]:
            answer+=1
            lim=targets[i][1]
    return answer