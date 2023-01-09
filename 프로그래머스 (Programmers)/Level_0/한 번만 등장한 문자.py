def solution(s):
    answer = ''
    answerAlphas=[]
    alphaHash=[0]*26
    for alpha in s:
        alphaHash[ord(alpha)-97]+=1
    for i in range(26):
        if alphaHash[i]==1:
            answerAlphas.append(chr(i+97))
    answerAlphas.sort()
    answer=''.join(answerAlphas)
    return answer