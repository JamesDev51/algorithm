bonuses={
    'S':1,
    'D':2,
    'T':3
}
options={
    '*':2,
    '#':-1
}
def solution(dartResult):
    scores=[0]*3
    trial=0;idx=0
    for trial in range(3):
        num=0
        while idx<len(dartResult) and dartResult[idx].isdigit():
            num*=10
            num+=int(dartResult[idx])
            idx+=1
        bonus=dartResult[idx];idx+=1
        scores[trial]+=int(num)
        scores[trial]=pow(scores[trial],bonuses[bonus])
        if idx<len(dartResult) and dartResult[idx] in "*#":
            option=dartResult[idx]
            if option=='*' and 0<=trial-1:scores[trial-1]*=options[option]
            scores[trial]*=options[option]
            idx+=1
    return sum(scores)