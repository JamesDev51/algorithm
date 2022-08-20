import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    sensors_gap=list()
    for i in range(1,n):
        sensors_gap.append(sensors[i]-sensors[i-1])
    sensors_gap.sort(reverse=True)
    res=(sensors[-1]-sensors[0])-(sum(sensors_gap[:k-1]))
    print(res)
    

if __name__=="__main__":
    n=int(input());k=int(input())
    sensors=list(map(int,input().split()))
    sensors.sort() 
    solve()
    