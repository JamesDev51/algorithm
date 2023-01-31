def solution(arr1, arr2):
    arr1_y,arr1_x=len(arr1),len(arr1[0])
    arr2_y,arr2_x=len(arr2),len(arr2[0])
    answer = [[0]*arr2_x for _ in range(arr1_y)]
    
    for y in range(arr1_y):
        for x in range(arr2_x):
            for mid in range(arr1_x):
                answer[y][x]+=arr1[y][mid]*arr2[mid][x]
    return answer