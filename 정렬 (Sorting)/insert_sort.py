import random

def insert_sort(A):
    result=[]
    while(A):
        num=A.pop(0) #가장 앞을 뽑아서
        result.append(num) #result의 가장 뒤에 넣기
        
        for i in range(len(result)-1,0,-1): #정렬된 곳 가장 뒤부터 가장 앞까지
            if(result[i]<result[i-1]): #num이 바로 앞의 수보다 클 때까지 교환해가면서 반복
                result[i],result[i-1]=result[i-1],result[i]
            else:break
    return result
        
    
if __name__=="__main__":
    num_list=list(range(1,21))
    random.shuffle(num_list)
    print("정렬 전 :",num_list)
    print("정렬 후 :",insert_sort(num_list))