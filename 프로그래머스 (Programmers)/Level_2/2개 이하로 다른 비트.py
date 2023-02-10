def solution(numbers):
    answer = []
    
    for number in numbers:
        if number%2==0:
            answer.append(number+1)
        else:
            bin_number_rev=bin(number)[:1:-1]+'0'
            for i in range(len(bin_number_rev)-1):
                if bin_number_rev[i]=='1' and bin_number_rev[i+1]=='0':
                    ans=bin_number_rev[:i]+'0'+'1'+bin_number_rev[i+2:]
                    answer.append(int(ans[::-1],2))
                    break

    return answer