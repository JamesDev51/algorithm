uid_nick_map=dict()
def init(record):
    for rec in record:
        splited_rec=rec.split(" ")
        com=splited_rec[0]
        if com=="Enter":
            uid,nick=splited_rec[1],splited_rec[2]
            uid_nick_map[uid]=nick
        elif com=="Change":
            uid,nick=splited_rec[1],splited_rec[2]
            uid_nick_map[uid]=nick
def solve(record):
    ret=[]
    for rec in record:
        splited_rec=rec.split(" ")
        com=splited_rec[0]
        if com=="Enter":
            uid,nick=splited_rec[1],splited_rec[2]
            msg=f"{uid_nick_map[uid]}님이 들어왔습니다."
            ret.append(msg)
        elif com=="Leave":
            uid=splited_rec[1]
            msg=f"{uid_nick_map[uid]}님이 나갔습니다."
            ret.append(msg)
    return ret
def solution(record):
    
    init(record)
    answer = solve(record)
    
    return answer