import math
def solution(begin, end):
    def calc_biggest_prime_number(number):
        if number==1:return 0
        ret=1
        for i in range(2,int(math.sqrt(number))+1):
            if number%i==0 and i<=1e7:
                ret=max(ret,i)
                if number//i<=1e7 and number//i !=number:
                    ret=max(ret,number//i)
                
        return ret
    answer=[]
    for num in range(begin,end+1):
        answer.append(calc_biggest_prime_number(num))
    return answer