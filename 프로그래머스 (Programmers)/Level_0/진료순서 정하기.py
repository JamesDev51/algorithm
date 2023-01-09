def solution(emergency):
    answer = [0]*(len(emergency))
    tmpList=[]
    for idx,val in enumerate(emergency):
        tmpList.append((val,idx))
    tmpList.sort(key=lambda x:-x[0])
    for idx,data in enumerate(tmpList):
        val,orgIdx=data
        answer[orgIdx]=idx+1
    return answer