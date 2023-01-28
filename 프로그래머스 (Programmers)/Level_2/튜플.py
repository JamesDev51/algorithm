def solution(s):
    
    tuples=[]
    tmp_ch=""
    for ch in s[1:-1]:
        if ch=="{":
            tmp_ch=""
        elif ch=="}":
            tmp_ch_list=list(map(int,tmp_ch.split(",")))
            tuples.append(tmp_ch_list)
            tmp_ch=""
        else:tmp_ch+=ch
    
    answer = []
    tuples.sort(key=lambda x:len(x))
    status=[0]*100001
    for now_tuple in tuples:
        now_status=[0]*100001
        for num in now_tuple:
            now_status[num]+=1
            if now_status[num]>status[num]:
                status[num]+=1
                answer.append(num)
                
    
    
    return answer