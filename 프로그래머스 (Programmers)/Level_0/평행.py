def getAcceleration(twoDots):
    y1,x1=twoDots[0]
    y2,x2=twoDots[1]
    yInc=y2-y1
    xInc=x2-x1
    return yInc/xInc
    
    

def solution(dots):
    for i in range(4):
        for j in range(i+1,4):
            if i!=j:
                com1=[dots[i],dots[j]]
                com2=[]
                for k in range(4):
                    if k not in [i,j]: com2.append(dots[k])
                if getAcceleration(com1)==getAcceleration(com2):
                    return 1
    return 0
                
                        
            
                
                
