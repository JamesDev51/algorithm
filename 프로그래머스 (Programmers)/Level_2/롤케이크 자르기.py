left_hash,right_hash=[0]*10001,[0]*10001
left,right=0,0
def init(topping):
    global left,right
    for idx in range(len(topping)):
        t=topping[idx]
        if right_hash[t]==0:right+=1
        right_hash[t]+=1
   
def solution(topping):
    global left,right
    answer = 0
    init(topping)
    for div_idx in range(1,len(topping)):
        change=topping[div_idx-1]
        if left_hash[change]==0:left+=1
        left_hash[change]+=1
        right_hash[change]-=1
        if right_hash[change]==0:right-=1
        if left==right:answer+=1
        
    
    return answer