month_dates={
    29:[2],
    30:[4,6,9,11],
    31:[1,3,5,7,8,10,12]
}
days=['FRI','SAT','SUN','MON','TUE','WED','THU']

def solution(a, b):
    total_date=b-1
    for month in range(1,a):
        for key,value in month_dates.items():
            if month in value:
                total_date+=key
    total_date%=7
    answer=days[total_date]
    return answer