# import the modules
import os
import time
from os import listdir

# get the path/directory
# folder_dir = "F:\iit_kgp_academics\mtp\Running_code\train\MildDemented images"


from PIL import Image
import math

def change_img(direction):
    # pictochange="other.jpg"
    pictochange=direction
    a=Image.open(pictochange)
    # a=Image.open('profile_pic3.jpg')

    for t in range(1):
        im = Image.open(pictochange).convert('RGB')
        # dm=[]
        dm=im.size
        length=dm[0]
        width=dm[1]

        nim=Image.new('RGB',(length,width))



        for i in range(length):
            for j in range(width):
                # print("("+str(i),end=' ')
                # print(str(j)+")",end=' ')
                tmpd=[255,255,255,255]
                tmpu=[255,255,255,255]
                tmpl=[255,255,255,255]
                tmpr=[255,255,255,255]
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
                # red=(tmpd[0]/count)+(tmpu[0]/count)+(tmpl[0]/count)+(tmpr[0]/count)
                red=min(tmpd[0],tmpu[0],tmpl[0],tmpr[0])
                # red=int(math.floor(red))
                # green=(tmpd[1]/count)+(tmpu[1]/count)+(tmpl[1]/count)+(tmpr[1]/count)
                # green=int(math.floor(green))
                green=min(tmpd[1],tmpu[1],tmpl[1],tmpr[1])

                # blue=(tmpd[2]/count)+(tmpu[2]/count)+(tmpl[2]/count)+(tmpr[2]/count)
                # blue=int(math.floor(blue))
                blue=min(tmpd[2],tmpu[2],tmpl[2],tmpr[2])

                nim.putpixel((i,j),(red,green,blue,255))

        # nim.save("final1.png")

        for i in range(length):
            for j in range(width):
                tmp=nim.getpixel((i,j))
                im.putpixel((i,j),tmp)
        
        # newname=pictochange.split('.')
        # newname.pop()
        # finalname=""
        # for i in newname:
        #     finalname=finalname+i
        # finalname=finalname+".jpg"
        # print(finalname)
        im.save(pictochange)
        # im.save(pictochange,quality=95, optimize=True)






main_folder="train_test_dataset_own_4x"
for bigfolders in os.listdir(main_folder):
    folder_dir = main_folder+"\\"+bigfolders 
    for folders in os.listdir(folder_dir):

        # check if the image ends with png
        # print(len(folders))
        count=0
        for images in os.listdir(folder_dir+"\\" + folders):
            count=count+1
            # if (images.endswith(".jpg")):
                # change_img(folder_dir+"\\"+folders+"\\"+images)
                # print(images)
                # time.sleep(0.1)
        print(count)
