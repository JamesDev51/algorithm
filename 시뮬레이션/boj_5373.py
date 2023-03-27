import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from copy import deepcopy

def init_cube():
    cube=[['']*9 for _ in range(12)]
    for y in range(3):
        for x in range(3):
            cube[y][3+x]='o'
            cube[3+y][x]='g'
            cube[3+y][3+x]='w'
            cube[3+y][6+x]='b'
            cube[6+y][3+x]='r'
            cube[9+y][3+x]='y'
    return cube

def up(direction):
    global cube
    cp_cube=deepcopy(cube)
    if direction=='+':
        for i in range(3):
            cp_cube[3+i][6]=cube[2][3+i]
            cp_cube[6][5-i]=cube[3+i][6]
            cp_cube[5-i][2]=cube[6][5-i]
            cp_cube[2][3+i]=cube[5-i][2]
            for j in range(3):cp_cube[j+3][2-i+3]=cube[i+3][j+3]
    else:
        for i in range(3):
            cp_cube[2][3+i]=cube[3+i][6]
            cp_cube[5-i][2]=cube[2][3+i]
            cp_cube[6][5-i]=cube[5-i][2]
            cp_cube[3+i][6]=cube[6][5-i]
            for j in range(3):cp_cube[i+3][j+3]=cube[j+3][2-i+3]
    cube=cp_cube
    
def down(direction):
    global cube
    cp_cube=deepcopy(cube)
    if direction=='+':
        for i in range(3):
            cp_cube[0][3+i]=cube[3+i][8]
            cp_cube[5-i][0]=cube[0][3+i]
            cp_cube[8][5-i]=cube[5-i][0]
            cp_cube[3+i][8]=cube[8][5-i]
            for j in range(3):cp_cube[j+9][2-i+3]=cube[i+9][j+3]
    else:
        for i in range(3):
            cp_cube[3+i][8]=cube[0][3+i]
            cp_cube[0][3+i]=cube[5-i][0]
            cp_cube[5-i][0]=cube[8][5-i]
            cp_cube[8][5-i]=cube[3+i][8]
            for j in range(3):cp_cube[i+9][j+3]=cube[j+9][2-i+3]
    cube=cp_cube
    
def front(direction):
    global cube
    cp_cube=deepcopy(cube)
    if direction=='+':
        for i in range(3):
            cp_cube[5][3+i]=cube[5][i]
            cp_cube[5][6+i]=cube[5][3+i]
            cp_cube[9][5-i]=cube[5][6+i]
            cp_cube[5][i]=cube[9][5-i]
            for j in range(3):cp_cube[j+6][2-i+3]=cube[i+6][j+3]
    else:
        for i in range(3):
            cp_cube[5][i]=cube[5][3+i]
            cp_cube[5][3+i]=cube[5][6+i]
            cp_cube[5][6+i]=cube[9][5-i]
            cp_cube[9][5-i]=cube[5][i]
            for j in range(3):cp_cube[i+6][j+3]=cube[j+6][2-i+3]
    cube=cp_cube
    
def back(direction):
    global cube
    cp_cube=deepcopy(cube)
    if direction=='+':
        for i in range(3):
            cp_cube[3][3+i]=cube[3][6+i]
            cp_cube[3][i]=cube[3][3+i]
            cp_cube[11][5-i]=cube[3][i]
            cp_cube[3][6+i]=cube[11][5-i]
            for j in range(3):cp_cube[j][2-i+3]=cube[i][j+3]
    else:
        for i in range(3):
            cp_cube[3][6+i]=cube[3][3+i]
            cp_cube[3][3+i]=cube[3][i]
            cp_cube[3][i]=cube[11][5-i]
            cp_cube[11][5-i]=cube[3][6+i]
            for j in range(3):cp_cube[i][j+3]=cube[j][2-i+3]
    cube=cp_cube

def left(direction):
    global cube
    cp_cube=deepcopy(cube)
    if direction=='+':
        for i in range(3):
            cp_cube[3+i][3]=cube[i][3]
            cp_cube[6+i][3]=cube[3+i][3]
            cp_cube[9+i][3]=cube[6+i][3]
            cp_cube[i][3]=cube[9+i][3]
            for j in range(3):cp_cube[j+3][2-i]=cube[i+3][j]
    else:
        for i in range(3):
            cp_cube[i][3]=cube[3+i][3]
            cp_cube[3+i][3]=cube[6+i][3]
            cp_cube[6+i][3]=cube[9+i][3]
            cp_cube[9+i][3]=cube[i][3]      
            for j in range(3):cp_cube[i+3][j]=cube[j+3][2-i]
    cube=cp_cube

def right(direction):
    global cube
    cp_cube=deepcopy(cube)
    if direction=='+':
        for i in range(3):
            cp_cube[2-i][5]=cube[5-i][5]
            cp_cube[5-i][5]=cube[8-i][5]
            cp_cube[8-i][5]=cube[11-i][5]
            cp_cube[11-i][5]=cube[2-i][5]
            for j in range(3):cp_cube[j+3][2-i+6]=cube[i+3][j+6]
    else:
        for i in range(3):
            cp_cube[5-i][5]=cube[2-i][5]
            cp_cube[8-i][5]=cube[5-i][5]
            cp_cube[11-i][5]=cube[8-i][5]
            cp_cube[2-i][5]=cube[11-i][5]
            for j in range(3):cp_cube[i+3][j+6]=cube[j+3][2-i+6]
    cube=cp_cube
if __name__=="__main__":
    for _ in range(int(input())):
        cube=init_cube()
        n=int(input())
        turns=list(input().split())
        
        for turn in turns:
            pos,direction=turn[0],turn[1]
            if pos=='U':up(direction)
            elif pos=='D':down(direction)
            elif pos=='F':front(direction)
            elif pos=='B':back(direction)
            elif pos=='L':left(direction)
            elif pos=='R':right(direction)
        for y in range(3,6):print(''.join(cube[y][3:6]))