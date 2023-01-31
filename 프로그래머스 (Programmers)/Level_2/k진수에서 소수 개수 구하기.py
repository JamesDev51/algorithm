from math import sqrt

def convert_num(n,k):
    ret=''
    while n:
        ret=str(n%k)+ret
        n//=k
    return ret

def check_prime(num):
    if num<2:return False
    if num==2:return True
    for i in range(2,int(sqrt(num)+1)):
        if num%i==0:return False
    return True

def solution(n, k):
    c_n=convert_num(n,k)+"0"
    answer=0
    
    tmp_num=""
    for num in c_n:
        if num!='0':tmp_num+=num
        else:
            if tmp_num!="" and check_prime(int(tmp_num)):answer+=1
            tmp_num=""
        
    return answer