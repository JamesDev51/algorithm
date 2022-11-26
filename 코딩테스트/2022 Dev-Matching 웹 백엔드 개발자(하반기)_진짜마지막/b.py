import math

def preProcess(record):
    recordDict=dict()
    for s in record:
        name,times=s.split(":")
        times=list(map(int,times.split(",")))
        recordDict[name]=times
    return recordDict

def calcMedal(record):
    medalDict=dict()
    for name in record.keys(): medalDict[name]=[0,0,0]

    for contest in range(5):
        completedRecord=[]
        for name,times in record.items():
            if times[contest]!=0: completedRecord.append((times[contest],name))
        size=len(completedRecord)
        completedRecord.sort()
        gold,silver,cop=int(math.ceil(size/12)),int(math.ceil(size/4)),int(math.ceil(size/2))
        for i in range(cop):
            if i<gold:medalDict[completedRecord[i][1]][0]+=1
            elif gold<=i<silver:medalDict[completedRecord[i][1]][1]+=1
            elif silver<=i<cop:medalDict[completedRecord[i][1]][2]+=1
    return medalDict
            
def solution(record):
    answer = []
    
    record=preProcess(record)
    medal=calcMedal(record)

    candidates=[]
    for name,times in record.items():
        completedCnt=0
        for i in range(5):
            if times[i]!=0: completedCnt+=1
        highestLevel=6
        for level in range(4,-1,-1):
                if record[name][level]!=0: highestLevel=level+1; break
        timeSum=sum(times)
        candidates.append((name,completedCnt,highestLevel,medal[name][0],medal[name][1],medal[name][2],timeSum))
    candidates.sort(key=lambda x:(-x[1],-x[2],-x[3],-x[4],-x[5],x[6],x[0]))
    for candidate in candidates: answer.append(candidate[0])
    
    return answer