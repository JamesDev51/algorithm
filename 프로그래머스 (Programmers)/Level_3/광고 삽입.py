def solution(play_time, adv_time, logs):
    def convert_time(time):
        hour,minute,seconds=map(int,time.split(":"))
        return hour*3600+minute*60+seconds
    def reverse_convert_time(time_seconds):
        tot_minutes=time_seconds//60
        seconds=time_seconds%60
        hour=tot_minutes//60
        minutes=tot_minutes%60
        hour_s="{0:02d}".format(hour)
        minutes_s="{0:02d}".format(minutes)
        seconds_s="{0:02d}".format(seconds)
        return hour_s+":"+minutes_s+":"+seconds_s
        
    answer = ''
    play_time_seconds=convert_time(play_time)
    adv_time_seconds=convert_time(adv_time)
    
    acc_play_time=[0]*(play_time_seconds+3)
    for log in logs:
        start_time,end_time=log.split("-")
        start_time_seconds=convert_time(start_time)
        end_time_seconds=convert_time(end_time)
        acc_play_time[start_time_seconds]+=1
        acc_play_time[end_time_seconds]-=1
    for t in range(1,play_time_seconds+2):
        acc_play_time[t]+=acc_play_time[t-1]
    for t in range(1,play_time_seconds+2):
        acc_play_time[t]+=acc_play_time[t-1]
    
    max_acc_seconds=float('-inf')
    max_acc_adv_start_time_seconds=0
    for adv_start_time in range(play_time_seconds-adv_time_seconds+2):
        acc_seconds=acc_play_time[adv_start_time+adv_time_seconds-1]-acc_play_time[adv_start_time-1]
        if max_acc_seconds<acc_seconds:
            max_acc_seconds=acc_seconds
            max_acc_adv_start_time_seconds=adv_start_time
    answer=reverse_convert_time(max_acc_adv_start_time_seconds)
        
    
    
    return answer