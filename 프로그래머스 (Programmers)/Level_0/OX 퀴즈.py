def solution(quiz):
    answer = []
    for q in quiz:
        left,right=q.split("=")
        right=int(right)
        leftSplited=left.strip().split(" ")
        num1,num2=int(leftSplited[0]),int(leftSplited[2])
        if leftSplited[1]=="+":answer.append("O" if num1+num2==right else "X") 
        else:answer.append("O" if num1-num2==right else "X")
    return answer