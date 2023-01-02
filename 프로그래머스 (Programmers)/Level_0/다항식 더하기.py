def solution(polynomial):
    answer = ''
    a,num=0,0
    for pol in polynomial.strip().split(" "):
        if pol=="+":continue
        if "x" in pol:
            if len(pol)==1: a+=1
            else: a+=int(pol[:-1])
        else: num+=int(pol)
    if a!=0 and num!=0: 
        answer=f"{a}x + {num}" if a!=1 else f"x + {num}"
    elif a!=0 and num==0: 
        answer=f"{a}x"  if a!=1 else f"x"
    elif a==0 and num!=0: answer=f"{num}"
    else: answer=0
    return answer