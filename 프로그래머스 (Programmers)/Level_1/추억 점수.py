def solution(name, yearning, photo):
    answer = []
    name_yearning=dict()
    for idx in range(len(name)):
        name_yearning[name[idx]]=yearning[idx]
    for photo_arr in photo:
        score=0
        for name in photo_arr:
            if name in name_yearning:
                score+=name_yearning[name]
        answer.append(score)
        
        
    return answer