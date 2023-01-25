def solution(brown, yellow):
    for row in range(3,5001):
        for col in range(3,5001):
            if row>=col and 2*row+2*col-4==brown and (row-2)*(col-2)==yellow:
                return [row,col]
