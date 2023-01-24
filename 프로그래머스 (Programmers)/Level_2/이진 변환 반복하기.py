def solution(s):
    answer = [0,0]
    while int(s,2)>1:
        zero_count=s.count('0')
        new_s_length=len(s)-zero_count
        s=bin(new_s_length)[2:]
        
        answer[0]+=1
        answer[1]+=zero_count
    return answer