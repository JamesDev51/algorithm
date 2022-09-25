import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    numbers=[254]
    answer = []
    for num in numbers:
        bin_num=bin(num)[2:]
        tree_size=0; i=1
        while tree_size<len(bin_num):tree_size=tree_size +i; i=i<<1
        while len(bin_num)<tree_size: bin_num='0'+bin_num
        flag=1
        print(tree_size)
        for i in range(1,len(bin_num),2):
            if bin_num[i]=='0':flag=0
        answer.append(flag)
    print(answer)