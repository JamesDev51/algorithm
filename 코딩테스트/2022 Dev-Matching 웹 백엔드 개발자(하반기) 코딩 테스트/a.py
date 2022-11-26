import sys
sys.stdin = open("input.text",  "rt")
import sys
from itertools import permutations
input=sys.stdin.readline

def solution(registered_list, new_id):
    if new_id not in registered_list: return new_id
    idx=0
    while idx<len(new_id) and new_id[idx].isalpha():idx+=1

    ss=new_id[:idx]
    nn=int(new_id[idx:]) if idx<len(new_id) else 0
    ch=[0]*(1000000)
    for registered_id in registered_list:
        if registered_id[:idx]==ss:
            n=int(registered_id[idx:]) if idx<len(registered_id) else 0
            ch[n]=1
    for i in range(nn+1,1000000):
        if not ch[i]: return ss+str(i)
            