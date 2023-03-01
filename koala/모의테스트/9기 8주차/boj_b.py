import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def test(password):
    flag_1,flag_2,flag_3=0,1,1;
    v_cnt,c_cnt=0,0
    last_ch=''; acc_cnt=0
    for ch in password:
        if ch in 'aeiou': 
            flag_1=1
            c_cnt=0;v_cnt+=1
        else:
            v_cnt=0;c_cnt+=1
    
        if last_ch==ch:
            acc_cnt+=1
            if acc_cnt==2:
                if last_ch*2 in ['ee','oo']:continue
                else:flag_3=0;break
        else:
            last_ch=ch; 
            acc_cnt=1
        if c_cnt==3 or v_cnt==3:
            flag_2=0;break
    return flag_1 and flag_2 and flag_3

if __name__=="__main__":
    while True:
        password=input().strip()
        if password=='end':break
        print(f"<{password}> is acceptable." if test(password) else f"<{password}> is not acceptable.")