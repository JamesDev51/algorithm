import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def init():
    for num in range(11,101):
        smallest=''
        while num:
            num-=7
            if num>=0:smallest+='8'
            else:num+=7;break
        small={2:'1', 5:'2', 6:'6'}
        if num in small:smallest=small[num]+smallest
        else:
            if num==1:smallest='10'+smallest[1:]
            elif num==3:smallest='200'+smallest[2:]
            elif num==4:smallest='20'+smallest[1:]
        ans.append(int(smallest))
    
if __name__=="__main__":
    ans=[0,0,1,7,4,2,6,8,10,18,22]
    init()
    for _ in range(int(input())):
        n=int(input())
        print(ans[n],end=" ")
        print('7'*(n%2)+'1'*(n//2-(n%2)))
        