def solution(s, skip, index):
    answer = ''
    
    for ch in s:
        cp_index=index
        while cp_index:
            if ord(ch)+1==123:new_ch='a'
            else:new_ch=chr(ord(ch)+1)
            if new_ch not in skip:
                cp_index-=1
            ch=new_ch
        answer+=new_ch

    return answer