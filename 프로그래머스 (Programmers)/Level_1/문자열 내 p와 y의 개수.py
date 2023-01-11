def solution(s):
    answer = True
    p,y=0,0
    for alp in s:
        if alp.lower()=="p":p+=1
        if alp.lower()=="y":y+=1

    return p==y