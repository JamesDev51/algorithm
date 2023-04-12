import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    a='''
Case #1: 0 2 4
Case #2: -1
    '''
    b='''
Case #1: 0 2 4
Case #2: -1
    '''
    print(a==b)