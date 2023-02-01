from math import ceil
car_status=dict()

def calculate_time(start,end):
    s_hour,s_min=map(int,start.split(":"))
    e_hour,e_min=map(int,end.split(":"))
    return (60*e_hour+e_min)-(60*s_hour+s_min)
    

def solution(fees, records):
    answer = []
    
    for record in records:
        time,car_num,div=record.split(" ")
        if car_num not in car_status:car_status[car_num]=[[div,time]]
        else:car_status[car_num].append([div,time])
    
    last_div=False
    for car_num,values in car_status.items():
        total_time=0
        for div,time in values:
            if div=="IN":
                last_div=True
                in_time=time
            else:
                last_div=False
                out_time=time
                total_time+=calculate_time(in_time,out_time)
                
        if last_div: #입차만 있고 출차가 없는 경우
            total_time+=calculate_time(in_time,"23:59")
        
        if total_time<=fees[0]: answer.append((car_num,fees[1]))
        else:answer.append((car_num,fees[1]+(ceil((total_time-fees[0])/fees[2])*fees[3])))
    answer.sort()
    answer=[answer[i][1] for i in range(len(answer))] 
        
    return answer