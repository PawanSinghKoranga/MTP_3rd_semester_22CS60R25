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



def generate_img(direction,finaldest):
    # direction=direction
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
            for j in range(math.floor(width/2)):
                temp=im.getpixel((i,width-j-1))
                nim.putpixel((i,j),im.getpixel((i,width-j-1)))
                nim.putpixel((i,width-j-1),im.getpixel((i,j)))
        
        nim.save(finaldest)


def generate_img_90deg(direction,finaldest):
    # direction=direction
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


        # for i in range(length):
        #     for j in range(math.floor(width/2)):
        #         temp=im.getpixel((i,width-j-1))
        #         nim.putpixel((i,j),im.getpixel((i,width-j-1)))
        #         nim.putpixel((i,width-j-1),im.getpixel((i,j)))

        for t in range(math.floor(length/15)):
            for  i in range(length):
                for j in range(width):
                    if((j+1)<width):
                        im.putpixel((i,j),im.getpixel((i,j+1)))


        N=max(length,width)
        for x in range(math.floor(N/2)):
            
            for y in range(x,N-x-1,1):
                if(x<length and y<width):
                    temp=im.getpixel((x,y))
                if(x<length and y<length and y<length and N-1-x<width):
                    im.putpixel((x,y),im.getpixel((y,N-1-x)))
                if(y<length and N-1-x<width and N-1-x<length and N-1-y<width):
                    im.putpixel((y,N-1-x),im.getpixel((N-1-x,N-1-y)))
                if(N-1-x<length and N-1-y<width and N-1-y<length and x<width):
                    im.putpixel((N-1-x,N-1-y),im.getpixel((N-1-y,x)))
                if(N-1-y<length and x<width and x<length and y<length):
                    im.putpixel((N-1-y,x),temp)
            # for j in range(math.floor(width/2)):
                # temp=im.getpixel((i,width-j-1))
                # nim.putpixel((i,j),im.getpixel((i,width-j-1)))
                # nim.putpixel((i,width-j-1),im.getpixel((i,j)))
        
        im.save(finaldest)
        # nim.save(finaldest)



        # for i in range(length):
        #     for j in range(width):
        #         # print("("+str(i),end=' ')
        #         # print(str(j)+")",end=' ')
        #         tmpd=[255,255,255,255]
        #         tmpu=[255,255,255,255]
        #         tmpl=[255,255,255,255]
        #         tmpr=[255,255,255,255]
        #         count=0
        #         if(i-1>=0):
        #             tmpd=im.getpixel((i-1,j))
        #             count=count+1
                
        #         if(i+1<length):
        #             tmpu=im.getpixel((i+1,j))
        #             count=count+1

        #         if(j-1>=0):    
        #             tmpl=im.getpixel((i,j-1))
        #             count=count+1

        #         if(j+1<width):    
        #             tmpr=im.getpixel((i,j+1))
        #             count=count+1

        #         # print("this is tmpd"+str(tmpd[0]))
        #         # red=(tmpd[0]/count)+(tmpu[0]/count)+(tmpl[0]/count)+(tmpr[0]/count)
        #         red=min(tmpd[0],tmpu[0],tmpl[0],tmpr[0])
        #         # red=int(math.floor(red))
        #         # green=(tmpd[1]/count)+(tmpu[1]/count)+(tmpl[1]/count)+(tmpr[1]/count)
        #         # green=int(math.floor(green))
        #         green=min(tmpd[1],tmpu[1],tmpl[1],tmpr[1])

        #         # blue=(tmpd[2]/count)+(tmpu[2]/count)+(tmpl[2]/count)+(tmpr[2]/count)
        #         # blue=int(math.floor(blue))
        #         blue=min(tmpd[2],tmpu[2],tmpl[2],tmpr[2])

        #         nim.putpixel((i,j),(red,green,blue,255))

        # # nim.save("final1.png")

        # for i in range(length):
        #     for j in range(width):
        #         tmp=nim.getpixel((i,j))
        #         im.putpixel((i,j),tmp)
        
        # # newname=pictochange.split('.')
        # # newname.pop()
        # # finalname=""
        # # for i in newname:
        # #     finalname=finalname+i
        # # finalname=finalname+".jpg"
        # # print(finalname)
        # im.save(pictochange)
        # # im.save(pictochange,quality=95, optimize=True)


main_folder="train_test_dataset_own_4x"
for bigfolders in os.listdir(main_folder):
    folder_dir = main_folder+"\\"+bigfolders 

    for folders in os.listdir(folder_dir):

        # check if the image ends with png
        # print(len(folders))
        print("we are bros")
        
        path=os.path.join(main_folder, "temp")
        if(os.path.exists(path)==False):
            os.mkdir(path)
        print("are we bros?")

        
        # k=0

        for images in os.listdir(folder_dir+"\\" + folders):
            
            # if (images.endswith(".jpg")):
                # change_img(folder_dir+"\\"+folders+"\\"+images)
                
                generate_img(folder_dir+"\\"+folders+"\\"+images,path+"\\"+"lr_"+images)
                generate_img_90deg(folder_dir+"\\"+folders+"\\"+images,path+"\\"+"90deg_"+images)
                # k=k+1
                # change_img(path)
                # print(images)
                # time.sleep(0.1)
        
        for images in os.listdir(path):
            src_path=os.path.join(path,images)
            dst_path=os.path.join(folder_dir+"\\" + folders,images)
            os.rename(src_path,dst_path)
            
                

        #copy to folder_dir+"\\"+folders
        if(os.path.exists(path)==True):
            os.rmdir(path)
