def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        tmpList=[]
        for j in range(i,i+n):
            tmpList.append(num_list[j])
        answer.append(tmpList)
    return answer