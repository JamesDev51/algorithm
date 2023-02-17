from itertools import combinations
course_cnt=dict()

def pre_operate(orders,course):
    for cnt in course:
        course_cnt[cnt]=dict()
    
    for order in orders:
        l_order=list(order)
        l_order.sort()
        for cnt in course:
            if len(order)<cnt:break
            for comb in combinations(l_order,cnt):
                course_dishes=''.join(comb)
                if course_dishes not in course_cnt[cnt]:course_cnt[cnt][course_dishes]=1
                else:course_cnt[cnt][course_dishes]+=1
def operate(course):
    res=[]
    for cnt in course:
        items=list(course_cnt[cnt].items())
        if not items:continue
        items.sort(key=lambda x:(-x[1]))
        largest=items[0][1]
        if largest<=1:continue
        idx=0
        while idx<len(items) and largest==items[idx][1]:
            res.append(items[idx][0])
            idx+=1
    res.sort()
    return res
        
def solution(orders, course):
    pre_operate(orders,course)
    res=operate(course)
    return res