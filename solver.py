# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:30:24 2018

@author: Ramsey
"""
import datetime
import copy
import random

def LU(Mylist):
    Mylist[0][0], Mylist[0][2] = Mylist[0][2], Mylist[0][0]
    Mylist[4][0], Mylist[4][2] = Mylist[4][2], Mylist[4][0]
    Mylist[2][0], Mylist[2][2] = Mylist[2][2], Mylist[2][0]
    Mylist[6][0], Mylist[6][2] = Mylist[6][2], Mylist[6][0]
    Mylist[4], Mylist[0], Mylist[6], Mylist[2] = Mylist[0], Mylist[2], Mylist[4], Mylist[6]
    return Mylist

def RU(Mylist):
    Mylist[1][0], Mylist[1][2] = Mylist[1][2], Mylist[1][0]
    Mylist[5][0], Mylist[5][2] = Mylist[5][2], Mylist[5][0]
    Mylist[7][0], Mylist[7][2] = Mylist[7][2], Mylist[7][0]
    Mylist[3][0], Mylist[3][2] = Mylist[3][2], Mylist[3][0]
    Mylist[1], Mylist[5], Mylist[7], Mylist[3] = Mylist[3], Mylist[1], Mylist[5], Mylist[7]
    return Mylist

def LD(Mylist):
    Mylist[0][0], Mylist[0][2] = Mylist[0][2], Mylist[0][0]
    Mylist[4][0], Mylist[4][2] = Mylist[4][2], Mylist[4][0]
    Mylist[2][0], Mylist[2][2] = Mylist[2][2], Mylist[2][0]
    Mylist[6][0], Mylist[6][2] = Mylist[6][2], Mylist[6][0]
    Mylist[0], Mylist[2], Mylist[4], Mylist[6] = Mylist[4], Mylist[0], Mylist[6], Mylist[2]
    return Mylist
    
def RD(Mylist):
    Mylist[1][0], Mylist[1][2] = Mylist[1][2], Mylist[1][0]
    Mylist[5][0], Mylist[5][2] = Mylist[5][2], Mylist[5][0]
    Mylist[7][0], Mylist[7][2] = Mylist[7][2], Mylist[7][0]
    Mylist[3][0], Mylist[3][2] = Mylist[3][2], Mylist[3][0]
    Mylist[1], Mylist[3], Mylist[5], Mylist[7] = Mylist[5], Mylist[1], Mylist[7], Mylist[3]
    return Mylist

def TL(Mylist):
    Mylist[0][1], Mylist[0][2] = Mylist[0][2], Mylist[0][1]
    Mylist[1][1], Mylist[1][2] = Mylist[1][2], Mylist[1][1]
    Mylist[4][1], Mylist[4][2] = Mylist[4][2], Mylist[4][1]
    Mylist[5][1], Mylist[5][2] = Mylist[5][2], Mylist[5][1]
    Mylist[0], Mylist[1], Mylist[4], Mylist[5] = Mylist[1], Mylist[5], Mylist[0], Mylist[4]
    return Mylist

def TR(Mylist):
    Mylist[0][1], Mylist[0][2] = Mylist[0][2], Mylist[0][1]
    Mylist[1][1], Mylist[1][2] = Mylist[1][2], Mylist[1][1]
    Mylist[4][1], Mylist[4][2] = Mylist[4][2], Mylist[4][1]
    Mylist[5][1], Mylist[5][2] = Mylist[5][2], Mylist[5][1]
    Mylist[0], Mylist[1], Mylist[4], Mylist[5] = Mylist[4], Mylist[0], Mylist[5], Mylist[1]
    return Mylist

def BoR(Mylist):
    Mylist[2][1], Mylist[2][2] = Mylist[2][2], Mylist[2][1]
    Mylist[3][1], Mylist[3][2] = Mylist[3][2], Mylist[3][1]
    Mylist[6][1], Mylist[6][2] = Mylist[6][2], Mylist[6][1]
    Mylist[7][1], Mylist[7][2] = Mylist[7][2], Mylist[7][1]
    Mylist[2], Mylist[3], Mylist[6], Mylist[7] = Mylist[6], Mylist[2], Mylist[7], Mylist[3]
    return Mylist

def BoL(Mylist):
    Mylist[2][1], Mylist[2][2] = Mylist[2][2], Mylist[2][1]
    Mylist[3][1], Mylist[3][2] = Mylist[3][2], Mylist[3][1]
    Mylist[6][1], Mylist[6][2] = Mylist[6][2], Mylist[6][1]
    Mylist[7][1], Mylist[7][2] = Mylist[7][2], Mylist[7][1]
    Mylist[2], Mylist[3], Mylist[6], Mylist[7] = Mylist[3], Mylist[7], Mylist[2], Mylist[6]
    return Mylist

def FR(Mylist):
    Mylist[0][0], Mylist[0][1] = Mylist[0][1], Mylist[0][0]
    Mylist[1][0], Mylist[1][1] = Mylist[1][1], Mylist[1][0]
    Mylist[2][0], Mylist[2][1] = Mylist[2][1], Mylist[2][0]
    Mylist[3][0], Mylist[3][1] = Mylist[3][1], Mylist[3][0]
    Mylist[0], Mylist[1], Mylist[2], Mylist[3] = Mylist[2], Mylist[0], Mylist[3], Mylist[1]
    return Mylist

def FL(Mylist):
    Mylist[0][0], Mylist[0][1] = Mylist[0][1], Mylist[0][0]
    Mylist[1][0], Mylist[1][1] = Mylist[1][1], Mylist[1][0]
    Mylist[2][0], Mylist[2][1] = Mylist[2][1], Mylist[2][0]
    Mylist[3][0], Mylist[3][1] = Mylist[3][1], Mylist[3][0]
    Mylist[0], Mylist[1], Mylist[2], Mylist[3] = Mylist[1], Mylist[3], Mylist[0], Mylist[2]
    return Mylist
    
def BaL(Mylist):
    Mylist[4][0], Mylist[4][1] = Mylist[4][1], Mylist[4][0]
    Mylist[5][0], Mylist[5][1] = Mylist[5][1], Mylist[5][0]
    Mylist[6][0], Mylist[6][1] = Mylist[6][1], Mylist[6][0]
    Mylist[7][0], Mylist[7][1] = Mylist[7][1], Mylist[7][0]
    Mylist[4], Mylist[5], Mylist[6], Mylist[7] = Mylist[5], Mylist[7], Mylist[4], Mylist[6]
    return Mylist

def BaR(Mylist):
    Mylist[4][0], Mylist[4][1] = Mylist[4][1], Mylist[4][0]
    Mylist[5][0], Mylist[5][1] = Mylist[5][1], Mylist[5][0]
    Mylist[6][0], Mylist[6][1] = Mylist[6][1], Mylist[6][0]
    Mylist[7][0], Mylist[7][1] = Mylist[7][1], Mylist[7][0]
    Mylist[4], Mylist[5], Mylist[6], Mylist[7] = Mylist[6], Mylist[4], Mylist[7], Mylist[5]
    return Mylist


def randomcube(cube):
    r = random.randint(1,12)
    print("Randomly rotated by: ", r)
    if r == 1:
        return LU(cube)
    elif r == 2:
        return LD(cube)
    elif r == 3:
        return RU(cube)
    elif r == 4:
        return RD(cube)
    elif r == 5:
        return TL(cube)
    elif r == 6:
        return TR(cube)
    elif r == 7:
        return BoL(cube)
    elif r == 8:
        return BoR(cube)
    elif r == 9:
        return FR(cube)
    elif r == 10:
        return FL(cube)
    elif r == 11:
        return BaR(cube)
    elif r == 12:
        return BaL(cube)
    
def perfectcube():
    cube = []
    for i in range(8):
        cube.append([0,0,0])
    cube[0][0] = 0
    cube[1][0] = 0
    cube[4][0] = 0
    cube[5][0] = 0
    cube[0][1] = 1
    cube[2][1] = 1
    cube[4][1] = 1
    cube[6][1] = 1
    cube[0][2] = 2
    cube[1][2] = 2
    cube[2][2] = 2
    cube[3][2] = 2
    cube[1][1] = 3
    cube[3][1] = 3
    cube[5][1] = 3
    cube[7][1] = 3
    cube[2][0] = 4
    cube[3][0] = 4
    cube[6][0] = 4
    cube[7][0] = 4
    cube[4][2] = 5
    cube[5][2] = 5
    cube[6][2] = 5
    cube[7][2] = 5
    return cube

def myprint(my):
    print("   ",my[4][0],my[5][0])
    print("   ",my[0][0],my[1][0])
    print(my[4][1], my[0][1], my[0][2], my[1][2], my[1][1], my[5][1], my[5][2], my[4][2])
    print(my[6][1], my[2][1], my[2][2], my[3][2], my[3][1], my[7][1], my[7][2], my[6][2])
    print("   ",my[2][0],my[3][0])
    print("   ",my[6][0],my[7][0])
# 0 to 7 is 
# 0 to 2
def is_solved(cube):
    #cube[i][j] = cube[i*3+j]
    #       12 15
    #       0  3
    #13 1   2  5   4 16 17 14
    #19 7   8 11   10 22 23 20
    #       6  9
    #       18 21
# 4 2 0     4 3 0    5 2 0
# 5 3 0     4 2 1    4 3 1
# 5 2 1     5 3 1
    checks = []
    checks.append(cube[0][0] == cube[1][0] and cube[0][0] == cube[4][0] and cube[0][0] == cube[5][0])
    checks.append(cube[0][1] == cube[2][1] and cube[0][1] == cube[4][1] and cube[0][1] == cube[6][1])
    checks.append(cube[0][2] == cube[1][2] and cube[0][2] == cube[2][2] and cube[0][2] == cube[3][2])
    checks.append(cube[1][1] == cube[3][1] and cube[1][1] == cube[5][1] and cube[1][1] == cube[7][1])
    checks.append(cube[2][0] == cube[3][0] and cube[2][0] == cube[6][0] and cube[2][0] == cube[7][0])   
    checks.append(cube[4][2] == cube[5][2] and cube[4][2] == cube[6][2] and cube[4][2] == cube[7][2])
    c = True
    for i in checks:
        c = c and i
   # print(checks)
    return c

def solver(cube, max_depth, pth):
    #print("solver: ",path)
    #myprint(cube)
    path = copy.deepcopy(pth)
    if is_solved(cube):
        return path
    if len(path) >= max_depth:
        return None
    #print(path)
    #LU, RU, LD, RD, TL, TR BoR, BoL, FR, FL, BaL, BaR
    newcube = copy.deepcopy(cube)
    newcube = LU(newcube)
    path.append("LU")
    solved = solver(newcube, max_depth, path)   
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = LD(newcube)
    path.append("LD")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = TL(newcube)
    path.append("TL")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = TR(newcube)
    path.append("TR")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = RU(newcube)
    path.append("RU")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = RD(newcube)
    path.append("RD")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = BoL(newcube)
    path.append("BoL")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = BoR(newcube)
    path.append("BoR")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = FR(newcube)
    path.append("FR")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = FL(newcube)
    path.append("FL")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = BaL(newcube)
    path.append("BaL")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    
    path = path[:-1]
    newcube = copy.deepcopy(cube)
    newcube = BaR(newcube)
    path.append("BaR")
    solved = solver(newcube, max_depth, path)
    if solved != None:
        return solved
    path = path[:-1]
    return None
        

def iter(cube):
    origcube = copy.deepcopy(cube)
    for i in range(8):
        start = time.time()
        print("Beginning range: ", i+1)
        cube = list(origcube)
        path = solver(cube, i+1, [])
        if path != None and path != []:
            print("HAVE A SOLUTION: depth = ", i+1 , "SOLUTION IS", path)
            return
        end = time.time()
        print("Time passed = [", end-start, "] seconds")

path = ["a","B","C"]

cube = perfectcube()

for i in range(6):
    cube = randomcube(cube)
myprint(cube)


print("---beforeiter")
myprint(cube)

iter(cube)



            