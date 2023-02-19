def convert(m):
    m_list=[]
    for ch in m:
        if ch=='#':m_list[-1]+=ch
        else:m_list.append(ch)
    return m_list

def check(m_list,melody_list):
    idx=0
    for tone in melody_list:
        if m_list[idx]==tone:idx+=1
        else:
            idx=0
            if m_list[idx]==tone:idx+=1
        
        if idx==len(m_list):return True
    return False

def solution(m, musicinfos):
    m_list=convert(m)
    res=[]
    for idx in range(len(musicinfos)):
        musicinfo=musicinfos[idx]
        start,end,title,melody=musicinfo.split(",")
        s_hour,s_min=map(int,start.split(":"))
        e_hour,e_min=map(int,end.split(":"))
        dur=abs((60*e_hour+e_min)-(60*s_hour+s_min))
        melody_list=convert(melody)
        real_melody_list=melody_list[:dur];m_idx=0
        while len(real_melody_list)<dur:
            real_melody_list.append(melody_list[m_idx])
            m_idx=(m_idx+1)%len(melody_list)
        if check(m_list,real_melody_list):
            res.append((dur,idx,title))
    res.sort(key=lambda x:(-x[0],x[1]))
    answer=res[0][2] if res else "(None)"
        
    return answer