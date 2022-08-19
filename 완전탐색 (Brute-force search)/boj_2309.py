import sys
sys.stdin = open("input.text",  "rt")
import sys
from itertools import combinations
input=sys.stdin.readline


if __name__=="__main__":
    boys=list(int(input()) for _ in range(9))
    for comb in combinations(boys,7):
        if sum(comb)==100:
            sorted_comb_list=sorted(list(comb))
            for boy in sorted_comb_list:print(boy)
            break
