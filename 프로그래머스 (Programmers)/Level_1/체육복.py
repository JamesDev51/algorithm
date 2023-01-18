def solution(n, lost, reserve):
    answer = n-len(lost)
    ch=[0]*(n+1)
    lost.sort()
    reserve.sort()
    for r_student in reserve:
        if r_student in lost:
            ch[r_student]=1
            answer+=1
    for l_student in lost:
        if ch[l_student]: continue #여벌있으면서 잃어버린 사람 (앞에서 처리함)
        front=l_student-1
        rear=l_student+1
        if 0<front and front in reserve and not ch[front]:
            ch[front]=1
            answer+=1
            continue
        if rear<=n and rear in reserve and not ch[rear]:
            ch[rear]=1
            answer+=1
            continue
    answer=min(answer,n)
    return answer