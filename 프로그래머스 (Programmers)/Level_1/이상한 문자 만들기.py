def solution(s):
    answer = ''
    word_idx=0
    for i in range(len(s)):
        if s[i].isalpha():
            if word_idx%2==0:answer+=s[i].upper()
            else:answer+=s[i].lower()
            word_idx+=1
        else:
            word_idx=0
            answer+=s[i]
    return answer