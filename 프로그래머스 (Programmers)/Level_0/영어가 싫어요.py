words=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    
def solution(numbers):
    answer = ''
    lt,rt=0,0
    while lt<=rt and lt<len(numbers):
        if numbers[lt:rt] not in words:
            rt+=1
        else:
            answer+=str(words.index(numbers[lt:rt]))
            lt=rt
    
    return int(answer)