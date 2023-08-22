def solution(genres, plays):
    answer = []
    genre_play=dict()
    genre_used=dict()
    n=len(genres)
    for i in range(n):
        genre=genres[i]
        play=plays[i]
        if genre not in genre_play:genre_play[genre]=play
        else: genre_play[genre]+=play
        
    genre_idx=dict()
    for idx,value in enumerate(sorted(list(genre_play.items()),key=lambda x:-x[1])):
        genre_idx[value[0]]=idx
        if idx not in genre_used:genre_used[idx]=0
    tmp=[]
    for i in range(n):
        genre=genres[i]
        play=plays[i]
        tmp.append([genre_idx[genre],play,i])
    tmp.sort(key=lambda x:(x[0],-x[1],x[2]))
    for genre,_,idx in tmp:
        if genre_used[genre]<2:
            answer.append(idx)
            genre_used[genre]+=1        
    return answer