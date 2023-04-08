import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init():
    for i in range(0,41,2):
        nodes[i]=i
        graph[i].append(i+2)
    #1,3,5
    nodes[1]=13;graph[10].append(1)
    nodes[3]=16;graph[1].append(3)
    nodes[5]=19;graph[3].append(5)
    graph[5].append(25)
    
    #7,9
    nodes[7]=22;graph[20].append(7)
    nodes[9]=24;graph[7].append(9)
    graph[9].append(25)
    
    #11,13,15
    nodes[11]=28;graph[30].append(11)
    nodes[13]=27;graph[11].append(13)
    nodes[15]=26;graph[13].append(15)
    graph[15].append(25)
    
    #25,27,29
    nodes[25]=25;graph[25].append(27)
    nodes[27]=30;graph[27].append(29)
    nodes[29]=35;graph[29].append(40)

def check():
    global res
    score=0
    horse_loc=[0]*4
    for i in range(10):
        dice,horse_idx=arr[i],dices[i]
        now_horse_loc=horse_loc[horse_idx]
        if now_horse_loc in [10,20,30]:new_horse_loc=graph[now_horse_loc][1];dice-=1
        else:new_horse_loc=now_horse_loc
        
        for _ in range(dice):
            if new_horse_loc==end:break
            new_horse_loc=graph[new_horse_loc][0]
            
        horse_loc[horse_idx]=new_horse_loc
        if new_horse_loc!=end:
            for other_horse_idx in range(4):
                if other_horse_idx==horse_idx:continue
                if horse_loc[other_horse_idx]==new_horse_loc:return
            score+=nodes[new_horse_loc]
    res=max(res,score)

def go(level):
    if level==10:
        check()
        return
    for horse_idx in range(4):
        dices[level]=horse_idx
        go(level+1)


if __name__=="__main__":
    start=0;end=42
    graph=[[] for _ in range(41)]
    nodes=[0]*41
    init()
    arr=list(map(int,input().split()))
    dices=[0]*10
    res=float('-inf')
    go(0)
    print(res)