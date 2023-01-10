def solution(chicken):
    answer = 0
    coupons=chicken
    while coupons>=10:
        now_order=(coupons//10)
        coupons%=10
        coupons+=now_order
        answer+=now_order
            
    return answer