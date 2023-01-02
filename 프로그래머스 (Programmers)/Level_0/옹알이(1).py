def solution(babbling):
    answer = 0
    words=['aya','ye','woo','ma']
    for babb in babbling:
        idx=0
        while True:
            flag=False
            for word in words:
                if babb[idx:idx+len(word)]==word:
                    idx+=len(word)
                    flag=True
                    break
            if not flag:break
        if idx==len(babb):answer+=1
    return answer