want_hash=dict()
sale_hash=dict()

def init(discount, want, number):
    for d_product in discount:
        want_hash[d_product]=0
        sale_hash[d_product]=0
    for w_product in want:
        want_hash[w_product]=0
        sale_hash[w_product]=0
    for i in range(len(want)):
        want_hash[want[i]]+=number[i]

def solution(want, number, discount):
    
    answer =0
    init(discount,want,number)
    total_size=sum(number)
    lt,rt=0,total_size
    for i in range(lt,rt): sale_hash[discount[i]]+=1
    
    if want_hash==sale_hash:answer+=1
    while rt<len(discount):
        lt_product=discount[lt]
        rt_product=discount[rt]
        sale_hash[lt_product]-=1; lt+=1
        sale_hash[rt_product]+=1; rt+=1
        if want_hash==sale_hash:answer+=1
    
    return answer