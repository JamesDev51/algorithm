ranks=[-1,6,5,4,3,2,0]

def solution(lottos, win_nums):
    answer = [0,0]
    same_count=0
    for lotto in lottos:
        if lotto in win_nums: same_count+=1
    for i in range(1,7):
        if ranks[i]<=same_count:answer[1]=i;break
    answer[0]=max(1,answer[1]-lottos.count(0))
        
    return answer