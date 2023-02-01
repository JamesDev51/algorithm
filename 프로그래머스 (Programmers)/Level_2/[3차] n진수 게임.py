hex_num={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def convert_num(num,d):
    if not num: return '0'
    ret=''
    while num:
        new_num=num%d
        if new_num>=10:ret=hex_num[new_num]+ret
        else:ret=str(new_num)+ret
        num//=d
    return ret

def solution(n, t, m, p):
    answer = ''

    idx=0; num=0
    while True:
        
        converted_num=convert_num(num,n)
        for ch in converted_num:
            if idx==p-1:answer+=ch
            if len(answer)==t:return answer
            idx=(idx+1)%m
        num+=1