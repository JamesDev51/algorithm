import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

able_dict=dict()

def dfs(k,tot):
    result=1 if tot==k else 0 #한자리 숫자
    if tot<k:
        for now_num,need in able_dict.items():
            if tot+need<=k: result+=dfs(k,tot+need)
    return result


def solution(k):
    answer = 0
    needs=[6,2,5,5,4,5,6,3,7,6]
    for idx,need in enumerate(needs):
        if need<=k: able_dict[idx]=need
    for s in range(10):
        if s==0 and k==6 and s in able_dict: answer+=1 #0이 가장 앞에 나오는 것을 방지
        if s!=0 and s in able_dict: answer+=dfs(k, able_dict[s]) #시작은 1~9
    return answer