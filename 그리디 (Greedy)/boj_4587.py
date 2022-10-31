import sys
sys.stdin = open("input.text",  "rt")
import sys
from math import gcd
input=sys.stdin.readline


if __name__=="__main__":
    while True:
        p,q=map(int, input().split())
        if not p and not q: break
        while p:
            largest=q//p
            if q%p:largest+=1 
            
            tmp_p=largest*p-q #새로운 분자
            tmp_q=largest*q #새로운 분모
            
                
            
            tmp_gcd=gcd(tmp_p,tmp_q)
            tmp_p //=tmp_gcd
            tmp_q //=tmp_gcd
            
            while tmp_q>=1000000:
                largest+=1
                tmp_p=largest*p-q #새로운 분자
                tmp_q=largest*q #새로운 분모
                tmp_gcd=gcd(tmp_p,tmp_q)
                tmp_p //=tmp_gcd
                tmp_q //=tmp_gcd

            p,q=tmp_p,tmp_q
            print(largest,end=" ")
        print()
            