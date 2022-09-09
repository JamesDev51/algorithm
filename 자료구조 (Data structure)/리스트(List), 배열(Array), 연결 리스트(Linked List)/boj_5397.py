import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    left,right=[],[]
    for com in logger:
        if com=="<":
            if left: right.append(left.pop())
        elif com==">":
            if right: left.append(right.pop())
        elif com=="-":
            if left: left.pop()
        else:
            left.append(com)
    return ''.join(left)+''.join(right[::-1])

if __name__=="__main__":
    for _ in range(int(input())):
        logger=input().strip()
        print(solve())