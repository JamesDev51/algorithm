def solution(my_string):
    answer = ''
    used=set()
    for s in my_string:
        if s not in used:
            answer+=s
            used.add(s)
    return answer