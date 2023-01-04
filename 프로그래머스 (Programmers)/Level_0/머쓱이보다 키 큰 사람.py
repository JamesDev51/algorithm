def solution(array, height):
    answer = 0
    for a in array:
        if a>height: answer+=1
    return answer