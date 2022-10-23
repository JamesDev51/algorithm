import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    ch=0
    for _ in range(int(input())):
        inp=input().split()
        if len(inp)==1: com=inp[0]
        else: com=inp[0]; num=int(inp[1])
        
        if com=="add": ch |= (1<<num)
        elif com=="remove": ch &= ~(1<<num)
        elif com=="check": print(1 if ch & (1<<num) else 0)
        elif com=="toggle":  ch ^= (1<<num)
        elif com=="all":  ch |= ((1<<21)-1)
        elif com=="empty": ch=0