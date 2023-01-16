def solution(s, n):
    answer = ''
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                offset=ord(ch)-65
                answer+=chr(65+(offset+n)%26)
            else: 
                offset=ord(ch)-97
                answer+=chr(97+(offset+n)%26)
        else: answer+=ch
    return answer