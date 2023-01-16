def solution(array, commands):
    answer = []
    for i,j,k in commands:
        tmp_array=array[i-1:j]
        tmp_array.sort()
        answer.append(tmp_array[k-1])
    return answer