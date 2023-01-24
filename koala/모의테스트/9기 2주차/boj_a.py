import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    x_1=int(input())
    y_standard=int(input())
    y_limit=int(input())
    y_extra=int(input())
    used=int(input())
    
    x_fee=x_1*used
    y_fee=y_standard + max(0,used-y_limit)*y_extra
    print(min(x_fee,y_fee))