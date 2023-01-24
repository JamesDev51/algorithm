def solution(s):
    answer = ''
    blank=True
    for ch in s:
        if ch!=" ":
            if blank:
                if ch.isalpha(): answer+=ch.upper()
                else:answer+=ch
                blank=False
            else: 
                if ch.isalpha():answer+=ch.lower()
                else:answer+=ch
        else:
            blank=True
            answer+=ch
        
        
    return answer