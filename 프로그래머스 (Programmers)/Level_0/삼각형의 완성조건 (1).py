def solution(sides):
    largest=max(sides)
    largestIdx=sides.index(largest)
    leftSum=0
    for i in range(3):
        if i!=largestIdx: leftSum+=sides[i]
    return 1 if leftSum>largest else 2