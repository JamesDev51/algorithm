from itertools import combinations

def check(column_comb,relation):
    tuples=set()
    for info in relation:
        tup=[]
        for idx in column_comb:
            tup.append(info[idx])
        tup=tuple(tup)
        if tup not in tuples:
            tuples.add(tup)
        else:return False
    return True

def solution(relation):
    
    row=len(relation);col=len(relation[0])
    column_idxs=list(range(col))
    candidates=[]
    
    for cnt in range(1,col+1):
        for column_comb in combinations(column_idxs,cnt):
            flag=True
            for candidate in candidates:
                dup_cnt=0
                for col in candidate:
                    if col in column_comb:dup_cnt+=1
                if dup_cnt==len(candidate):flag=False;break
                
            if flag and check(column_comb,relation):
                candidates.append(column_comb)
    return len(candidates)