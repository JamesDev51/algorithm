def solution(cards):
    size=len(cards)
    ch=[0]*size
    group=1
    candidate=[]
    for i in range(size):
        if ch[i]:continue
        cnt=0
        now=i
        while not ch[now]:
            ch[now]=1
            cnt+=1
            now=cards[now]-1
        candidate.append(cnt)
        group+=1
    candidate.sort(reverse=True)
    return candidate[0]*candidate[1] if 1<len(candidate) else 0