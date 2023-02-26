import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    cipher=input().strip()
    words=list(input().strip() for _ in range(int(input())))
    for i in range(26):
        plaintext=''
        for ch in cipher:
            plaintext+=chr((ord(ch)-97+i)%26+97)
        for word in words:
            if word in plaintext:
                print(plaintext)
                exit(0)
    