def solution(dots):
    max_y,max_x=float('-inf'), float('-inf')
    min_y,min_x=float('inf'), float('inf')
    for y,x in dots:
        max_y=max(max_y,y)
        min_y=min(min_y,y)
        max_x=max(max_x,x)
        min_x=min(min_x,x)
    answer=(max_y-min_y)*(max_x-min_x)
    return answer