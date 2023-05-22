def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x :(x[col-1],-x[0]))
    
    tmp=[]
    for i in range(1,len(data)+1):
        sub_sum=0
        for j in range(len(data[0])):
            sub_sum+=data[i-1][j]%i
        tmp.append(sub_sum)
    answer=tmp[row_begin-1]
    for i in range(row_begin,row_end):
        answer^=tmp[i]
    
    return answer