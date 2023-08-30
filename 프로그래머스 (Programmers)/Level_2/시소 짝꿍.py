from collections import Counter
from math import comb
def solution(weights):
    answer = 0
    counter=Counter(weights)
    for weight1,count1 in counter.items():
        if count1>=2:answer+=comb(count1,2)
        for weight2,count2 in counter.items():
            flag=False
            if weight1>=weight2:continue
            for dist1 in range(2,5):
                for dist2 in range(2,5):
                    if weight1*dist1==weight2*dist2:
                        answer+=count1*count2
                        flag=True
                        break
                if flag:continue
                    
        
    return answer