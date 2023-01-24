def solution(s):
    splited_s=list(map(int,(s.split(" "))))
    answer = str(min(splited_s))+" "+str(max(splited_s))
    return answer