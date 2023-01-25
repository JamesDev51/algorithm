def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    lt,rt=0,len(people)-1
    while lt<=rt:
        if people[lt]+people[rt]<=limit:
            answer+=1;
            lt+=1;rt-=1
        else:
            lt+=1; answer+=1
    return answer