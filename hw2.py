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


for i in range(int(width*height/2)):
        newPixel.append((Pixel[6*i] + Pixel[6*i+3])/2)
        newPixel.append((Pixel[6*i+1] + Pixel[6*i+4])/2)
        newPixel.append((Pixel[6*i+2] + Pixel[6*i+5])/2)

width = int(width/2)
newPixel = list(map(int, newPixel))
newfile = open(newfilename, "w")

newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(newPixel[3*i*width+3*j])+" ")
        newfile.write(str(newPixel[3*i*width+3*j+1])+" ")
        newfile.write(str(newPixel[3*i*width+3*j+2])+" ")
    newfile.write("\n")

newfile.close()
    
