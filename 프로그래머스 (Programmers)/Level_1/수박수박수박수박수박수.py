def solution(n):
    flag=True
    answer = ''
    for _ in range(n):
        if flag:answer+='수';flag=False
        else: answer+='박';flag=True
    return answer