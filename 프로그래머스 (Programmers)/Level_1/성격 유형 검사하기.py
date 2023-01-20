partners=["RT","CF","JM","AN"]
scores={
    'R':0,
    'T':0,
    'C':0,
    'F':0,
    'J':0,
    'M':0,
    'A':0,
    'N':0
}

def solution(survey, choices):
    answer = ''
    for i in range(len(survey)):
        sur=survey[i]; choice=choices[i]
        l,r=sur[0],sur[1]

        if 1<=choice<=3:
            scores[l]+=(4-choice)
        elif 5<=choice<=7:
            scores[r]+=(choice%4)
        else: continue
    for part in partners:
        l,r=part[0],part[1]
        if scores[l]>=scores[r]:answer+=l
        else:answer+=r
    return answer