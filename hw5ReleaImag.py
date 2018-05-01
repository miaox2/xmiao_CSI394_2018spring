filename = input("Which ppm file you want to choose:")
newfilename = input("What file name you want to output:")
file = open(filename)
print(filename)

typeoffile = file.readline()

print(typeoffile)
WandH = file.readline()
t = WandH.split()
print(t)
width = t[0]
height = t[1]

print("width is: ",width, "height is: ", height)

numberofcolors = file.readline()


Colors = file.read()
file.close()
Pixel = list(Colors.split()) 
temp0 = int(0)

i=0
#Pixel = [0, 5]
j = len(Pixel)
print(i, j)
while i < j:
    if abs(float(Pixel[i])) < 0.00001:
        temp0 = float(Pixel[i+1])
        if temp0 > 1:
            Pixel.pop(i+1)
            Pixel.insert(i+1, 0)
            temp0 = temp0 - 1
            Pixel.insert(i+2, temp0)
            print(Pixel)
        elif temp0 == 1:
            Pixel.pop(i+1)
    i = i + 1 
    j = len(Pixel)
       
print(len(Pixel))        
newfile = open(newfilename, "w")
newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(len(Pixel)):
    newfile.write(str(Pixel[i])+"\n")
    
newfile.close()
