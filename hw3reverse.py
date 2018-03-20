filename = input("Which ppm file you want to choose:")
newfilename = input("What file name you want to output:")
file = open(filename)
print(filename)

typeoffile = file.readline()

print(typeoffile)
WandH = file.readline()
t = WandH.split()
width =int(t[0])
height =int(t[1])

print("width is: ",width, "height is: ", height)


numberofcolors = file.readline()

print("How many color pixels: ", numberofcolors)

Colors = file.read()
file.close()
Pixel = list(map(float, Colors.split()))
topPixel = []
botPixel = []
BefAveHeighPix = []
leftPixel = []
rightPixel = []
BefAveWidthPix = []

for i in range(int(3*height*width/2)):
    topPixel.append(Pixel[i]+Pixel[int((3*width*height/2) + i)])
    botPixel.append(2*Pixel[i] - topPixel[i])

for j in range(int(height/2)):
    for k in range(width):
        BefAveHeighPix.append(topPixel[3*k + 3*width*j])
        BefAveHeighPix.append(topPixel[3*k + 3*width*j +1])
        BefAveHeighPix.append(topPixel[3*k + 3*width*j +2])
    for k in range(width):
        BefAveHeighPix.append(botPixel[3*k + 3*width*j])
        BefAveHeighPix.append(botPixel[3*k + 3*width*j +1])
        BefAveHeighPix.append(botPixel[3*k + 3*width*j +2])
        
for i in range(height):
    for j in range(int(width/2)):
        leftPixel.append(BefAveHeighPix[3*i*width + 3*j] +BefAveHeighPix[3*i*width + 3*j + 3*width//2])
        rightPixel.append(2*BefAveHeighPix[3*i*width + 3*j] - leftPixel[3*i*width//2 +3*j])
        leftPixel.append(BefAveHeighPix[3*i*width + 3*j+1] +BefAveHeighPix[3*i*width + 3*j + 3*width//2 +1])
        rightPixel.append(2*BefAveHeighPix[3*i*width + 3*j+1] - leftPixel[3*i*width//2 +3*j+1])
        leftPixel.append(BefAveHeighPix[3*i*width + 3*j+2] +BefAveHeighPix[3*i*width + 3*j + 3*width//2 +2])
        rightPixel.append(2*BefAveHeighPix[3*i*width + 3*j+2] - leftPixel[3*i*width//2 +3*j+2])
        
for i in range(height):
    for j in range(int(width/2)):
        BefAveWidthPix.append(leftPixel[3*j +3*i*width//2])
        BefAveWidthPix.append(leftPixel[3*j +3*i*width//2 + 1])
        BefAveWidthPix.append(leftPixel[3*j +3*i*width//2 + 2])
    
        BefAveWidthPix.append(rightPixel[3*j +3*i*width//2])
        BefAveWidthPix.append(rightPixel[3*j +3*i*width//2 + 1])
        BefAveWidthPix.append(rightPixel[3*j +3*i*width//2 + 2])
        

newfile = open(newfilename, "w")

newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(int(BefAveWidthPix[3*i*width+3*j]))+" ")
        newfile.write(str(int(BefAveWidthPix[3*i*width+3*j+1]))+" ")
        newfile.write(str(int(BefAveWidthPix[3*i*width+3*j+2]))+" ")
    newfile.write("\n")

newfile.close()