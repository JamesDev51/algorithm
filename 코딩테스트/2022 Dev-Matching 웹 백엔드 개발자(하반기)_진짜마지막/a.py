def check(sy,sx,size,img):
    cnt=0

    row,col=len(img),len(img[0])
    for y in range(sy,sy+size):
        for x in range(sx,sx+size):
            if y==sy or y==sy+size-1 or x==sx or x==sx+size-1:
                if img[y][x]=='.':return -1
                else: continue
            else:
                if img[y][x]=='#': cnt+=1
    percent=cnt/pow(size-2,2)*100
    return percent

def solution(low, high, img):

    answer=0
    
    row,col=len(img),len(img[0])

    for size in range(3,row+1):
        for y in range(row-size+1):
            for x in range(col-size+1):
                ret=check(y,x,size,img)
                if ret!=-1 and low<=ret<high: answer+=1
    return answer
                    