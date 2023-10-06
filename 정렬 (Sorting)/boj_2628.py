import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    width,height=map(int,input().split())
    rows=[0,height]
    cols=[0,width]
    for _ in range(int(input())):
        div,a=map(int,input().split())
        if div==0:
            rows.append(a)
        else:
            cols.append(a)
    rows.sort()
    cols.sort()
    width_list,height_list=[],[]
    for i in range(len(cols)-1):
        width_list.append(cols[i+1]-cols[i])
    for i in range(len(rows)-1):
        height_list.append(rows[i+1]-rows[i])
    
    print(max(width_list)*max(height_list))
        
    