def first(new_id):
    return new_id.lower()

def second(new_id):
    new_id_2=''
    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch in "-_.": new_id_2+=ch
    return new_id_2

def third(new_id):
    new_id_3=''
    flag=False
    idx=0
    while idx<len(new_id):
        if new_id[idx]!='.':new_id_3+=new_id[idx]
        else:
            if idx+1<len(new_id) and new_id[idx+1]!='.':new_id_3+=new_id[idx]
        idx+=1
    return new_id_3
    
def fourth(new_id):
    return new_id.lstrip(".").rstrip(".")
    
def fifth(new_id):
    return "a" if not new_id else new_id
    
def sixth(new_id):
    new_id_6=new_id[:15]
    return new_id_6.rstrip(".")
def seventh(new_id):
    new_id_7=new_id
    while len(new_id_7)<3:new_id_7+=new_id[-1]
    return new_id_7    

def solution(new_id):
    new_id=first(new_id)
    new_id=second(new_id)
    new_id=third(new_id)
    new_id=fourth(new_id)
    new_id=fifth(new_id)
    new_id=sixth(new_id)
    new_id=seventh(new_id)
    print(new_id)
    answer=new_id
    return answer