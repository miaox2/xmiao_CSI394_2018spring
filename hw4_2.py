filename = input("Which image you want to read:")

file = open(filename)

typeoffile = file.readline()

WandH = file.readline()
t = WandH.split()
width =int(t[0])
height =int(t[1])

print("width is: ",width, "height is: ", height)

numberofcolors = file.readline()

Colors = file.read()
file.close()
Pixel = list(map(int, Colors.split()))

for i in range(int(len(Pixel)/3)):
    n1 = Pixel[3*i]%3
    n2 = Pixel[3*i+1]%3
    n3 = Pixel[3*i+2]%3
    
    if n1 == 0 and n2 == 0 and n3 == 0:
        print("!")
    else:
        q = n3 + 3*n2 + 9*n1
        c = chr(q + ord('a')-1)
        print(c)

