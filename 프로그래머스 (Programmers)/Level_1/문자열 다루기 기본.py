def solution(s):
    answer = True
    for ch in s:
        if not ch.isdigit():answer=False;break
    return answer if answer and len(s) in [4,6] else False