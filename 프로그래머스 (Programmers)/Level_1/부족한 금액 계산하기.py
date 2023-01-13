def solution(price, money, count):
    total_price=0
    for i in range(1,count+1): total_price+=price*i
    return total_price-money if total_price-money>0 else 0