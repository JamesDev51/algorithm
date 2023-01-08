def solution(my_string, num1, num2):
    if num1<num2:
        answer = my_string[:num1]+my_string[num2]+my_string[num1+1:num2]+my_string[num1]+my_string[num2+1:]
    else:
        answer = my_string[:num2]+my_string[num1]+my_string[num2+1:num1]+my_string[num2]+my_string[num1+1:]
    return answer