def get_day_count(full_date):
    year,month,date=map(int,full_date.split("."))
    return 28*12*year+28*month+date
    
    

def solution(today, terms, privacies):
    answer = []
    today_count=get_day_count(today)
    terms_dict=dict()
    
    for term in terms:
        alpha,month=term.split(" ")
        terms_dict[alpha]=int(month)
    
    for i in range(len(privacies)):
        privacy=privacies[i]
        full_date, term = privacy.split(" ")
        date_count=get_day_count(full_date)
        ex_date=date_count+terms_dict[term]*28
        if ex_date<=today_count: answer.append(i+1)
    
    
    return answer