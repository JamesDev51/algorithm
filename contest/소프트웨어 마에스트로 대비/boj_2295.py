import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n=int(input())
    u=list(int(input()) for _ in range(n))
    u.sort()
    
    ab=list()
    dc=list()
    dc_dict=dict()
    for num1 in u:
        for num2 in u:
            ab.append(num1+num2)
            if num1-num2>0: 
                dc.append(num1-num2)
                if num1-num2 in dc_dict:dc_dict[num1-num2]=max(dc_dict[num1-num2],num2)
                else:dc_dict[num1-num2]=num2
    ab=set(ab)
    dc=list(set(dc))
    dc.sort(reverse=True)
    res=-1
    for num in dc:
        if num in ab:
            res=max(res,num+dc_dict[num])
    print(res)
        