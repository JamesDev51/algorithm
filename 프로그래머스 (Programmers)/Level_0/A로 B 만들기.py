def solution(before, after):
    answer = 0
    beforeHash=[0]*26
    afterHash=[0]*26
    for s in before:
        beforeHash[ord(s)-97]+=1
    for s in after:
        afterHash[ord(s)-97]+=1    
    return answer if beforeHash!=afterHash else 1