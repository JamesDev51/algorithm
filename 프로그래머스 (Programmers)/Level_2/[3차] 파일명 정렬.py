def encode(files):
    encoded_files=[]
    for idx in range(len(files)):
        file=files[idx]
        number_start=False
        head,number,tail='',0,''
        
        for ch in file:
            if ch.isdigit():
                if not number_start: #처음 number시작
                    number_start=True
                    number=10*number+int(ch)
                else:
                    if tail=='': #아직 number임
                        number=10*number+int(ch)
                    else:
                        tail+=ch
            else:
                if not number_start:head+=ch.lower()
                else: tail+=ch
        encoded_files.append((head,number,idx,file))
    return encoded_files
                        
                

def solution(files):
    answer = []
    
    encoded_files=encode(files)
    encoded_files.sort()
    for _,_,_,file in encoded_files: answer.append(file)
    return answer