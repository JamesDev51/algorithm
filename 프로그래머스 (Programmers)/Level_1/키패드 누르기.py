num_pos=dict()

def get_dist(pos1,pos2):
    return abs(pos2[0]-pos1[0])+abs(pos2[1]-pos1[1])

def solution(numbers, hand):
    answer = ''
    LP,RP=[3,0],[3,2]
    num_pos[0]=[3,1]
    for num in range(9):num_pos[num+1]=[num//3,num%3]
    
    for num in numbers:
        if num in [1,4,7]:
            answer+='L'
            LP=num_pos[num]
        elif num in [3,6,9]:
            answer+='R'
            RP=num_pos[num]
        else:
            LD=get_dist(LP,num_pos[num])
            RD=get_dist(RP,num_pos[num])
            if LD>RD:
                answer+='R'
                RP=num_pos[num]
            elif LD<RD:
                answer+='L'
                LP=num_pos[num]
            else:
                if hand=='left':
                    answer+='L'
                    LP=num_pos[num]
                else:
                    answer+='R'
                    RP=num_pos[num]

    return answer