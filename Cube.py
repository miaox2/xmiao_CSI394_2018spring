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


def myprint(my):
    print("   ",my[4][0],my[5][0])
    print("   ",my[0][0],my[1][0])
    print(my[4][1], my[0][1], my[0][2], my[1][2], my[1][1], my[5][1], my[5][2], my[4][2])
    print(my[6][1], my[2][1], my[2][2], my[3][2], my[3][1], my[7][1], my[7][2], my[6][2])
    print("   ",my[2][0],my[3][0])
    print("   ",my[6][0],my[7][0])

def pic(Mylist):
    newList = []
    newList.append(6)
    newList.append(6)
    newList.append(Mylist[4][0])
    newList.append(Mylist[5][0])
    newList.append(6)
    newList.append(6)
    newList.append(6)      
    newList.append(6)
    
    newList.append(6)
    newList.append(6)       
    newList.append(Mylist[0][0])      
    newList.append(Mylist[1][0])
    newList.append(6)
    newList.append(6)      
    newList.append(6)      
    newList.append(6)       
    
    newList.append(Mylist[4][1])     
    newList.append(Mylist[0][1])
    newList.append(Mylist[0][2])  
    newList.append(Mylist[1][2])  
    newList.append(Mylist[1][1])  
    newList.append(Mylist[5][1])  
    newList.append(Mylist[5][2])
    newList.append(Mylist[4][2])
    
    newList.append(Mylist[6][1])
    newList.append(Mylist[2][1])
    newList.append(Mylist[2][2])
    newList.append(Mylist[3][2])
    newList.append(Mylist[3][1])
    newList.append(Mylist[7][1])
    newList.append(Mylist[7][2])
    newList.append(Mylist[6][2])
    
    newList.append(6)
    newList.append(6)
    newList.append(Mylist[2][0])
    newList.append(Mylist[3][0])
    newList.append(6)
    newList.append(6)
    newList.append(6)
    newList.append(6)
    
    newList.append(6)
    newList.append(6)
    newList.append(Mylist[6][0])
    newList.append(Mylist[7][0])
    newList.append(6)
    newList.append(6)
    newList.append(6)
    newList.append(6)
    
    PixList = []
    for i in range(len(newList)):
        if int(newList[i]) == 0:
            PixList.append(255)
            PixList.append(255)
            PixList.append(255)
        elif int(newList[i]) == 1:
            PixList.append(255)
            PixList.append(255)
            PixList.append(0)
        elif int(newList[i]) == 2:
            PixList.append(0)
            PixList.append(255)
            PixList.append(0)
        elif int(newList[i]) == 3:
            PixList.append(0)
            PixList.append(191)
            PixList.append(255)
        elif int(newList[i]) == 4:
            PixList.append(255)
            PixList.append(140)
            PixList.append(0)
        elif int(newList[i]) == 5:
            PixList.append(255)
            PixList.append(0)
            PixList.append(0)
        elif int(newList[i]) == 6:
            PixList.append(0)
            PixList.append(0)
            PixList.append(0)
        else:
            print(i, newList[i], "error of the cube")
        
    return PixList

def picreading(Mylist):
    newList = []
    for i in range(48):
        if int(Mylist[3*i]) ==255 and int(Mylist[3*i+1]) ==255 and int(Mylist[3*i+2]) ==255:
            newList.append(0)
        elif int(Mylist[3*i]) ==255 and int(Mylist[3*i+1]) ==255 and int(Mylist[3*i+2]) ==0:
            newList.append(1)
        elif int(Mylist[3*i]) ==0 and int(Mylist[3*i+1]) ==255 and int(Mylist[3*i+2]) ==0:
            newList.append(2)
        elif int(Mylist[3*i]) ==0 and int(Mylist[3*i+1]) ==191 and int(Mylist[3*i+2]) ==255:
            newList.append(3)
        elif int(Mylist[3*i]) ==255 and int(Mylist[3*i+1]) ==140 and int(Mylist[3*i+2]) ==0:
            newList.append(4)
        elif int(Mylist[3*i]) ==255 and int(Mylist[3*i+1]) ==0 and int(Mylist[3*i+2]) ==0:
            newList.append(5)
        elif int(Mylist[3*i]) ==0 and int(Mylist[3*i+1]) ==0 and int(Mylist[3*i+2]) ==0:
            newList.append(6)
        else:
            print("the wrong pix number.")
    twodiList = []
    for i in range(8):
        twodiList.append([0, 0, 0])
    
    twodiList[4][0] = newList[2]
    twodiList[5][0] = newList[3]
    
    twodiList[0][0] = newList[10]
    twodiList[1][0] = newList[11]
    
    twodiList[4][1] = newList[16]
    twodiList[0][1] = newList[17]
    twodiList[0][2] = newList[18]
    twodiList[1][2] = newList[19]
    twodiList[1][1] = newList[20]
    twodiList[5][1] = newList[21]
    twodiList[5][2] = newList[22]
    twodiList[4][2] = newList[23]
    
    twodiList[6][1] = newList[24]
    twodiList[2][1] = newList[25]
    twodiList[2][2] = newList[26]
    twodiList[3][2] = newList[27]
    twodiList[3][1] = newList[28]
    twodiList[7][1] = newList[29]
    twodiList[7][2] = newList[30]
    twodiList[6][2] = newList[31]
    
    twodiList[2][0] = newList[34]
    twodiList[3][0] = newList[35]
    
    twodiList[6][0] = newList[42]
    twodiList[7][0] = newList[43]
    
    return twodiList
        
        

### Initialize the image of cube
positions = []
for i in range(8):
    positions.append([])
    for j in range(3):
        positions[i].append(i*3+j)

myprint(positions)

cubeinput1 = input("Input the cube section 1, 0 = white, 1 = yellow, 2 = green, 3 = blue, 4 = orange, 5 = red: ")
Cube = cubeinput1.split(" ")
print(len(Cube),Cube)
    
newCube = []
for i in range(8):
    newCube.append([0,0,0])
for i in range(8):
    for j in range(3):
        newCube[i][j] = Cube[i*3+j]

myprint(newCube)
imageList = list(pic(newCube))

newfilename = input("Name the output image:")

width = 8
height = 6

newfile = open(newfilename, "w")

newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(imageList[3*i*width+3*j])+" ")
        newfile.write(str(imageList[3*i*width+3*j+1])+" ")
        newfile.write(str(imageList[3*i*width+3*j+2])+" ")
    newfile.write("\n")

newfile.close()


### Input the images
filename = input("Which cube ppm file you want to choose:")
file = open(filename)

typeoffile = file.readline()

WandH = file.readline()
t = WandH.split()
width =int(t[0])
height =int(t[1])
numberofcolors = file.readline()

Colors = file.read()
file.close()
Pixel = list(map(int, Colors.split()))

newCube = picreading(Pixel)

stepinput = input("what step do you want to do (LU RU LD RD TL TR BoL BoR FR FL BaL BaR)(enter 'done' to finish the step):")

while stepinput != "done":
    
    if stepinput == 'LU':
        newCube = LU(newCube)
    if stepinput == 'RU':
        newCube = RU(newCube)
    if stepinput == 'LD':
        newCube = LD(newCube)
    if stepinput == 'RD':
        newCube = RD(newCube)
    if stepinput == 'TL':
        newCube = TL(newCube)
    if stepinput == 'TR':
        newCube = TR(newCube)
    if stepinput == 'BoL':
        newCube = BoL(newCube)
    if stepinput == 'BoR':
        newCube = BoR(newCube)
    if stepinput == 'FR':
        newCube = FR(newCube)
    if stepinput == 'FL':
        newCube = FL(newCube)
    if stepinput == 'BaL':
        newCube = BaL(newCube)
    if stepinput == 'BaR':
        newCube = BaR(newCube)
        
    stepinput = input("what step do you want to do (LU RU LD RD TL TR BoL BoR FR FL BaL BaR)(enter 'done' to finish the step):")
    

imageList = list(pic(newCube))

### Output the images
newfilename = input("Name the output image:")

width = 8
height = 6

newfile = open(newfilename, "w")

newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(imageList[3*i*width+3*j])+" ")
        newfile.write(str(imageList[3*i*width+3*j+1])+" ")
        newfile.write(str(imageList[3*i*width+3*j+2])+" ")
    newfile.write("\n")

newfile.close()