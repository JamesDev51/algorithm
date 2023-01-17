voca={
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if not s[i].isalpha():
            answer*=10
            answer+=int(s[i])
        for num in voca.keys():
            if num==s[i:i+len(num)]:
                answer*=10
                answer+=voca[num]
                i+=(len(num)-1)
                
    return answer