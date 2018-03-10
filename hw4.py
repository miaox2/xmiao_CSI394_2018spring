message = input("Enter the Message:")

filename = input("input image:")
newfilename = input("Name of the output image:")
file = open(filename)

typeoffile = file.readline()

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

Mess = list(message)

for i in range(len(Mess)):
    R= Pixel[3*i] % 3
    G= Pixel[3*i+1] % 3
    B= Pixel[3*i+2] % 3
    
    if ord(Mess[i]) - ord('a')< 27 and ord(Mess[i]) - ord('a')> -1:
        n = ord(Mess[i]) - ord('a') + 1
        n1 = (int(int(n/3)/3))%3
        n2 = int(n/3)%3
        n3 = n%3
    else:
        n1 = 0
        n2 = 0
        n3 = 0
    
    if R - n1 == 1:
        if Pixel[3*i] > 253:
            Pixel[3*i] = Pixel[3*i] -1
        else:
            Pixel[3*i] = Pixel[3*i] +2
    elif R - n1 == 2:
        if Pixel[3*i] > 253:
            Pixel[3*i] = Pixel[3*i] -2
        else:
            Pixel[3*i] = Pixel[3*i] +1
    elif R - n1 == -1:
        if Pixel[3*i] > 253:
            Pixel[3*i] = Pixel[3*i] -2
        else:
            Pixel[3*i] = Pixel[3*i] +1
    elif R - n1 == -2:
        if Pixel[3*i] > 253:
            Pixel[3*i] = Pixel[3*i] -1
        else:
            Pixel[3*i] = Pixel[3*i] +2

    if G - n2 == 1:
        if Pixel[3*i+1] > 253:
            Pixel[3*i+1] = Pixel[3*i+1] -1
        else:
            Pixel[3*i+1] = Pixel[3*i+1] +2
    elif G - n2 == 2:
        if Pixel[3*i+1] > 253:
            Pixel[3*i+1] = Pixel[3*i+1] -2
        else:
            Pixel[3*i+1] = Pixel[3*i+1] +1
    elif G - n2 == -1:
        if Pixel[3*i+1] > 253:
            Pixel[3*i+1] = Pixel[3*i+1] -2
        else:
            Pixel[3*i+1] = Pixel[3*i+1] +1
    elif G - n2 == -2:
        if Pixel[3*i+1] > 253:
            Pixel[3*i+1] = Pixel[3*i+1] -1
        else:
            Pixel[3*i+1] = Pixel[3*i+1] +2
            
    if B - n3 == 1:
        if Pixel[3*i+2] > 253:
            Pixel[3*i+2] = Pixel[3*i+2] -1
        else:
            Pixel[3*i+2] = Pixel[3*i+2] +2
    elif B - n3 == 2:
        if Pixel[3*i+2] > 253:
            Pixel[3*i+2] = Pixel[3*i+2] -2
        else:
            Pixel[3*i+2] = Pixel[3*i+2] +1
    elif B - n3 == -1:
        if Pixel[3*i+2] > 253:
            Pixel[3*i+2] = Pixel[3*i+2] -2
        else:
            Pixel[3*i+2] = Pixel[3*i+2] +1
    elif B - n3 == -2:
        if Pixel[3*i+2] > 253:
            Pixel[3*i+2] = Pixel[3*i+2] -1
        else:
            Pixel[3*i+2] = Pixel[3*i+2] +2

newfile = open(newfilename, "w")

newfile.write("P3\n")
newfile.write(str(width)+" "+str(height)+"\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(Pixel[3*i*width+3*j])+" ")
        newfile.write(str(Pixel[3*i*width+3*j+1])+" ")
        newfile.write(str(Pixel[3*i*width+3*j+2])+" ")
    newfile.write("\n")

newfile.close()
            
    
    
    