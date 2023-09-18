from bisect import bisect_left
def solution(info, query):
    info_tree=dict()
    def tracking(l,presets,conditions):
        if l==4:
            sub_info_tree=info_tree
            score=conditions[-1]
            for preset in presets:
                sub_info_tree=sub_info_tree[preset]
            idx=bisect_left(sub_info_tree,score)
            return len(sub_info_tree)-idx
            
        ret=0
        sub_info_tree=info_tree
        for preset in presets:
            sub_info_tree=sub_info_tree[preset]
        condition=conditions[l]
        if condition=="-":
            for poss_key in sub_info_tree.keys():
                ret+=tracking(l+1,presets+[poss_key],conditions)
        else:
            if condition in sub_info_tree.keys():ret+=tracking(l+1,presets+[condition],conditions)
            else:return 0
        return ret
    answer = []
    for i in info:
        lang,part,career,food,score=i.split(" ")
        if lang not in info_tree:info_tree[lang]=dict()
        if part not in info_tree[lang]:info_tree[lang][part]=dict()
        if career not in info_tree[lang][part]:info_tree[lang][part][career]=dict()
        if food not in info_tree[lang][part][career]:info_tree[lang][part][career][food]=[]
        info_tree[lang][part][career][food].append(int(score))
    for lang_key in info_tree.keys():
        for part_key in info_tree[lang_key].keys():
            for career_key in info_tree[lang_key][part_key].keys():
                for food_key in info_tree[lang_key][part_key][career_key].keys():
                    info_tree[lang_key][part_key][career_key][food_key].sort()
    for q in query:
        lang,part,career,food_score=q.split(" and ")
        food,score=food_score.split(" ")
        score=int(score)
        answer.append(tracking(0,[],[lang,part,career,food,score]))
        
        
    return answer