import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    p_alpha=dict()
    for word in word_list:
        for idx in range(1,len(word)+1):
            alpha=word[-idx]
            if alpha not in p_alpha: p_alpha[alpha]=pow(10,idx-1)
            else: p_alpha[alpha]+=pow(10,idx-1)
    s_p_alpha=sorted(p_alpha.items(),key=lambda x :(-x[1],x[0]))
    
    res=0
    num=9
    for alpha,prime in s_p_alpha:
        res+=(prime*num)
        num-=1
    return res

if __name__=="__main__":
    n=int(input())
    word_list=[input().strip() for _ in range(n)]
    print(solve())