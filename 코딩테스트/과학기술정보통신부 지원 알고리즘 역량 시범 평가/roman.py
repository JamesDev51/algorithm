import sys
input=sys.stdin.readline


if __name__=="__main__":
    dic=dict()
    dic['I']=1
    dic['V']=5
    dic['X']=10
    dic['L']=50
    dic['C']=100
    dic['IV']=4
    dic['IX']=9
    dic['XL']=40
    dic['XC']=90
    
    s=input().strip()
    res=0
    idx=0
    while idx<len(s):
        if idx<len(s)-1 and dic.get(s[idx:idx+2])!=None:
            res+=dic[s[idx:idx+2]]
            idx+=2
            continue
        res+=dic[s[idx]]
        idx+=1
    print(res)