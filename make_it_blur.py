from PIL import Image
import math
pictochange="pwnpic.JPG"
a=Image.open(pictochange)
# a=Image.open('profile_pic3.jpg')

for t in range(200):
    im = Image.open(pictochange).convert('RGBA')
    # dm=[]
    dm=im.size
    length=dm[0]
    width=dm[1]

    nim=Image.new('RGBA',(length,width))



    for i in range(length):
        for j in range(width):
            # print("("+str(i),end=' ')
            # print(str(j)+")",end=' ')
            tmpd=[0,0,0,0]
            tmpu=[0,0,0,0]
            tmpl=[0,0,0,0]
            tmpr=[0,0,0,0]
            count=0
            if(i-1>=0):
                tmpd=im.getpixel((i-1,j))
                count=count+1
            
            if(i+1<length):
                tmpu=im.getpixel((i+1,j))
                count=count+1

            if(j-1>=0):    
                tmpl=im.getpixel((i,j-1))
                count=count+1

            if(j+1<width):    
                tmpr=im.getpixel((i,j+1))
                count=count+1

            # print("this is tmpd"+str(tmpd[0]))
            red=(tmpd[0]/count)+(tmpu[0]/count)+(tmpl[0]/count)+(tmpr[0]/count)
            red=int(math.floor(red))
            green=(tmpd[1]/count)+(tmpu[1]/count)+(tmpl[1]/count)+(tmpr[1]/count)
            green=int(math.floor(green))
            blue=(tmpd[2]/count)+(tmpu[2]/count)+(tmpl[2]/count)+(tmpr[2]/count)
            blue=int(math.floor(blue))
            nim.putpixel((i,j),(red,green,blue,255))

    nim.save("final1.JPG")

    for i in range(length):
        for j in range(width):
            tmp=nim.getpixel((i,j))
            im.putpixel((i,j),tmp)
    im.save(pictochange)
