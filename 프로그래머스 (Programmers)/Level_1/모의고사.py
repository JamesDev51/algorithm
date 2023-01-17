supos=[
    [1,2,3,4,5],
    [2,1,2,3,2,4,2,5],
    [3,3,1,1,2,2,4,4,5,5]
]

def solution(answers):
    res = []
    idx=[0,0,0]
    count=[0,0,0]
    for answer in answers:
        for i in range(3):
            if answer==supos[i][idx[i]]:
                count[i]+=1
            idx[i]=(idx[i]+1)%len(supos[i])
    max_right=max(count)
    for idx,value in enumerate(count):
        if value==max_right: 
            res.append(idx+1)
        
    return res