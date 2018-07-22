import cv2

def surounding_negatives(image):
    [width, height,rgb] = image.shape
    crop_img = image[y:y+h, x:x+w]
    list_of_negative_images[0]=image[0:coordinates[1],0:coordinates[0]]
    list_of_negative_images[1]=image[0:coordinates[1],coordinates[0]:coordinates[0]+coordinates[2]]
    list_of_negative_images[2]=image[0:coordinates[1],coordinates[0]+coordinates[2]:w-coordinates[0]-coordinates[2]]

    list_of_negative_images[3]=image[coordinates[1]:coordinates[1]+coordinates[3],0:coordinates[0]]
    list_of_negative_images[4]=image[coordinates[1]:coordinates[1]+coordinates[3],coordinates[0]+coordinates[2]:w-coordinates[0]-coordinates[2]]

    list_of_negative_images[5]=image[coordinates[1]+coordinates[3]:h-coordinates[1]+coordinates[3],0:coordinates[0]]
    list_of_negative_images[6]=image[coordinates[1]+coordinates[3]:h-coordinates[1]+coordinates[3],coordinates[0]:coordinates[0]+coordinates[2]]
    list_of_negative_images[7]=image[coordinates[1]+coordinates[3]:h-coordinates[1]+coordinates[3],coordinates[0]+coordinates[2]:w-coordinates[0]-coordinates[2]]

    return list_of_negative_images
