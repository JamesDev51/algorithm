import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    answer=0
    prev_skills=[0,0]
    
    for skill in s:
        if skill.isdigit(): answer+=1
        else:
            if skill=='L':prev_skills[0]+=1
            elif skill=='S': prev_skills[1]+=1
            elif skill=='R' and prev_skills[0]>0:answer+=1; prev_skills[0]-=1
            elif skill=='K' and prev_skills[1]>0: answer+=1; prev_skills[1]-=1
            else:break
    return answer

if __name__=="__main__":
    n=int(input())
    s=input().strip()
    print(solve())