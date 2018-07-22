import sys
import os
import cv2
from PIL import Image
import image_create

#def create_images(image,coordinates,min_size,max_size,number_of_crops,mode):
#	.....
#	return list_of_negative_images



def help():
    print "This function:"
    print "-create negative images by cropping possitive images from idir and puts the to the given folder ndir"
    print "-makes the bg.txt file"

    print "Optional parameters:"

    print "-idir [info_dir] : directory to info.lst file"
    print "-ndir [negatives_dir] : directory to the negative images folder"
    print "-bgdir [bg_dir] : directory to the bg file"
    print "-gray [true] : true or false for grayscale"
    print "-min_size [min_size] : minimum size of cropped images"
    print "-max_size [max_size] : maximum size of cropped images"
    print "-mode [number_of_mode] : 0 for random 1 for specific"
    print "-crops [number_of_crops] : the number of crops you want to generate"
    sys.exit()

def error(message):
    print message
    sys.exit()

def get_system_arguments():

    length=len(sys.argv)
    i=0

    global info_dir,negatives_dir,min_size,max_size,mode,number_of_crops,bg_dir,gray

    while(i<length):
        if(sys.argv[i]=="-idir"):
            info_dir=sys.argv[i+1]
        elif(sys.argv[i]=="-ndir"):
            negatives_dir=sys.argv[i+1]
        elif(sys.argv[i]=="-bgdir"):
            bg_dir=sys.argv[i+1]
        elif(sys.argv[i]=="-gray"):
            gray=sys.argv[i+1]
        elif(sys.argv[i]=="-min_size"):
            min_size=sys.argv[i+1]
        elif(sys.argv[i]=="max_size"):
            max_size=sys.argv[i+1]
        elif(sys.argv[i]=="-mode"):
            mode=int(sys.argv[i+1])
        elif(sys.argv[i]=="crops"):
            number_of_crops=sys.argv[i+1]
        elif(sys.argv[i]=="-help"):
            help()
        i=i+1


#Given a path; home/piyi/folder/lala returns : lala
def find_name(path):
	words=path.split("/")
	return words[-1]


#Given a line of the info.lst file returnss a list with the wanted parameters
def create_parameters(line):
    global min_size,max_size,number_of_crops,mode
    words= line.split(" ")
    image= cv2.imread(words[0])
    name=find_name(words[0])
    words[2]=int(words[2])
    words[3]=int(words[3])
    words[4]=int(words[4])
    words[5]=int(words[5])
    coordinates=[[words[3],words[2],words[5],words[4]]]
    parameters=[image,name,coordinates,min_size,max_size,number_of_crops,mode]

    #show the face
    #face_image=image[words[3]:words[3]+words[5],words[2]:words[2]+words[4]]
    #cv2.imshow("ntajei",face_image)

    return parameters

def make_negative_images(f):
    global mode,gray
    lines=f.readlines()
    for line in lines:
        print line
        parameters=create_parameters(line)
        print parameters[2]
        #sys.exit()
        neg_images=image_create.create_images(parameters[0],parameters[2],parameters[3],parameters[4],parameters[5],parameters[6],gray)
        i=0
        if(neg_images is None):
            print "NAOUME"
        print "hello"
        for image in neg_images:
            j=str(i)
            cv2.imwrite(negatives_dir+j+'-'+parameters[1],image)
            i=i+1


def bg_create():

    global negatives_dir,bg_dir

    f=open(bg_dir+"bg.txt","w")

    for file in os.listdir(negatives_dir):
        if file.endswith(".jpg" or ".jpeg" or "png"):
            f.write("negatives_dir"+file+"\n")
    f.close()


#default arguments
negatives_dir="/home/piyi/LOGGERHEADER/training_cascade/make_negatives/test/negatives/"
info_dir="/home/piyi/LOGGERHEADER/training_cascade/make_negatives/test/info.lst"
bg_dir="/home/piyi/LOGGERHEADER/training_cascade/make_negatives/test/"
min_size=100
max_size=400
number_of_crops=10
mode=0
gray=True

#Input arguments
get_system_arguments()

#negative images
f=open(info_dir,"r")
make_negative_images(f)
f.close()

#writing bg file
bg_create()
