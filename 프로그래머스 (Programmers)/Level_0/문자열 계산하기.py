def solution(my_string):
    answer = 0
    tmp_num=0
    operator=True
    for s in my_string:
        if s==" ":continue
        elif s.isdigit():
            tmp_num*=10
            tmp_num+=int(s)
        else:
            if operator: answer+=tmp_num
            else: answer-=tmp_num
            tmp_num=0    
            if s=="+":operator=True
            else: operator=False
    if operator: answer+=tmp_num
    else: answer-=tmp_num
        
    return answer