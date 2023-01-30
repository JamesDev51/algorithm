ch=[0]*8
answer=0
def check(piro,dungeons,explored,level):
    global answer
    answer=max(answer,explored)
    if level==len(dungeons): return
    for i in range(len(dungeons)):
        need,use=dungeons[i]
        if not ch[i] and need<=piro:
            ch[i]=1
            check(piro-use,dungeons,explored+1,level+1)
            ch[i]=0

def solution(k, dungeons):
    global answer
    check(k,dungeons,0,0)
    return answer