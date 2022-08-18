import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    infos=[list(map(int,input().split())) for _ in range(11)]
    infos.sort()
    taken=0; penalty=0
    for t,v in infos:
        taken+=t
        penalty+=(taken+20*v)
    print(penalty)