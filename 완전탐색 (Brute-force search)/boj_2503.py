import sys
sys.stdin = open("input.text",  "rt")
import copy
import sys
input=sys.stdin.readline

def check(now_num,st,ball):
    global poss_list
    str_now_num=str(now_num)
    new_poss_list=[]
    for num in poss_list:
        str_num=str(num)
        tmp_st,tmp_ball=0,0
        for i in range(3):
            for j in range(3):
                if str_now_num[i]==str_num[j]:
                     if i==j: tmp_st+=1
                     else: tmp_ball+=1
        if st==tmp_st and ball==tmp_ball:new_poss_list.append(num)
    poss_list=copy.deepcopy(new_poss_list)
        
if __name__=="__main__":
    n=int(input())
    poss_list=[]
    for num in range(100,1000):
        str_num=str(num)
        if '0' not in str_num and len(set(list(str_num)))==3:poss_list.append(num)
    for _ in range(n):
        num,st,ball=map(int,input().split())
        check(num,st,ball)
    print(len(poss_list))