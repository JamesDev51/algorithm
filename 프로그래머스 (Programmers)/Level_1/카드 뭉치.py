from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    que1=deque(cards1)
    que2=deque(cards2)
    for word in goal:
        if que1 and que1[0]==word:
            que1.popleft()
        elif que2 and que2[0]==word:
            que2.popleft()
        else:
            answer='No'
            break
    return answer