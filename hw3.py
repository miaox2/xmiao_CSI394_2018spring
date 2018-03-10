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
Pixel = list(map(int, Colors.split()))
print(Pixel)  
newPixel = []
newPixelaveH = []

for i in range(int(width*height/2)):
    newPixel.append((Pixel[6*i] + Pixel[6*i+3])/2)
    newPixel.append((Pixel[6*i+1] + Pixel[6*i+4])/2)
    newPixel.append((Pixel[6*i+2] + Pixel[6*i+5])/2)
width = int(width/2)
print(newPixel)  

for m in range(int(height/2)):
    for n in range(width):
        newPixelaveH.append((newPixel[2*m*3*width+3*n] + newPixel[2*m*3*width+3*n+3*width])/2)
        newPixelaveH.append((newPixel[2*m*3*width+3*n] + newPixel[2*m*3*width+3*n+3*width+1])/2)
        newPixelaveH.append((newPixel[2*m*3*width+3*n] + newPixel[2*m*3*width+3*n+3*width+2])/2)

height = int(height/2)
print(newPixelaveH)


newfile = open(newfilename, "w")

newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(newPixelaveH[3*i*width+3*j])+" ")
        newfile.write(str(newPixelaveH[3*i*width+3*j+1])+" ")
        newfile.write(str(newPixelaveH[3*i*width+3*j+2])+" ")
    newfile.write("\n")

newfile.close()
    