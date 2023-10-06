import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    answer=-1
    now_cnt=0
    for _ in range(10):
        out_cnt,in_cnt=map(int,input().split())
        now_cnt+=in_cnt
        now_cnt-=out_cnt
        answer=max(answer,now_cnt)
    print(answer)