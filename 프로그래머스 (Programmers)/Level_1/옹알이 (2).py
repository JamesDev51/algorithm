def solution(babbling):
    answer = 0
    able=["aya", "ye", "woo", "ma" ]
    for babb in babbling:
        last_used=[-10]*4 #이전에 사용했는지 체크
        flag=False
        idx=0
        while idx<len(babb):
            flag=False
            for j in range(4):
                ab=able[j]
                if babb[idx:idx+len(ab)]==ab and last_used[j]+len(ab)!=idx: 
                    last_used[j]=idx
                    idx+=(len(ab))
                    flag=True
                    break
            if not flag:break
        if flag:answer+=1
    return answer