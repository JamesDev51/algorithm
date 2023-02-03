def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx=0;flag=True
        for s in skill_tree:
            if s in skill:
                if s==skill[idx]:idx+=1
                else:flag=False;break
        if flag:answer+=1
        
    return answer