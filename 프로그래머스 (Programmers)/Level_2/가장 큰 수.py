def solution(numbers):
    str_numbers=list(map(str,numbers))
    arr=[]
    if set(str_numbers)=={"0"}:str_numbers=['0']
    for str_num in str_numbers:
        new_str_num=str_num
        while len(new_str_num)<4:new_str_num+=str_num[0]
        arr.append((new_str_num,str_num[-1],str_num))
    arr.sort(key=lambda x:(-int(x[0]),-int(x[1])))
    answer=""
    for _,_,num in arr:answer+=num
            

    return answer