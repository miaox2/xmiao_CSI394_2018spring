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


Colors = file.read()
file.close()
Pixel = list(Colors.split())
CompressedList = []
temp0 = int(0)

Threshold = float(input ("what threshold do you want to use?"))


for i in range(len(Pixel)):
    if abs(float(Pixel[i])) < Threshold:
    #-Threshold <= float(Pixel[i]) and float(Pixel[i]) <= Threshold:
        temp0 = temp0 + 1
    else:
        if temp0 > 0: 
        #i-1 >= 0 and -Threshold <= float(Pixel[i-1]) and float(Pixel[i-1]) <= Threshold:
            CompressedList.append(0)
            CompressedList.append(temp0)
            temp0 = 0
        CompressedList.append(Pixel[i])
    
if temp0 != 0:
    CompressedList.append(0)
    CompressedList.append(temp0)  
    
print("pix",len(Pixel))
print("len",len(CompressedList))
print("ct0",CompressedList.count(0))

newfile = open(newfilename, "w")
newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(len(CompressedList)):
    newfile.write(str(CompressedList[i])+" ")
    
newfile.close()
