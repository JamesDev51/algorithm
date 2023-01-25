def solution(n, words):
    answer = [0,0]

    turn=1
    prev=words[0][0]
    used=set()
    user_idx=0;word_idx=0
    while word_idx<len(words):
        now_word=words[word_idx]
        if now_word not in used and prev==now_word[0]:
            used.add(now_word)
            prev=now_word[-1]
            word_idx+=1; 
            if user_idx+1==n: turn+=1; user_idx=0
            else: user_idx+=1
        else:
            answer=[user_idx+1,turn]
            break
    
    return answer