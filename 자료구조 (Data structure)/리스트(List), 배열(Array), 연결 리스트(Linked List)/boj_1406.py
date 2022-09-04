import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


if __name__=="__main__":
    left,right=list(input().strip()),list()
    n=int(input())
    for _ in range(n):
        command=input().strip()
        if command=="L" and left: right.append(left.pop())
        elif command=="D" and right: left.append(right.pop())
        elif command=="B" and left: left.pop() 
        elif command[0]=="P": left.append(command[-1])
    print(''.join(left)+''.join(right[::-1]))