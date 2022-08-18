import sys
sys.stdin = open("input.text",  "rt")
import sys
from itertools import combinations, combinations_with_replacement
input=sys.stdin.readline


def check(num):
    for comb in combinations_with_replacement(samgaksu_list,3):
        if sum(comb)==num: return  True
    return False
def make_samgaksu():
    samgaksu_list=[]
    num=2; samgaksu=1
    while samgaksu<=1000:
        samgaksu_list.append(samgaksu)
        samgaksu+=num
        num+=1
    return samgaksu_list    

if __name__=="__main__":
    n=int(input())
    samgaksu_list=make_samgaksu()
    for _ in range(n):
        num=int(input())
        print(1 if check(num) else 0)
    