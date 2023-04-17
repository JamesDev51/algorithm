import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    i=1
    while pow(2,i)<n:n-=pow(2,i);i+=1
    n-=1
    bin_n=bin(n)[2:]
    bin_n='0'*(i-len(bin_n))+bin_n
    res=''
    for ch in bin_n:
        if ch=='0':res+='4'
        else:res+='7'
    print(res)
    
    