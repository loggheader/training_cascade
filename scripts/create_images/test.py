import imgcreate
import cv2



img=cv2.imread("/home/mpourmpoulis/Pictures/turtles/t-1.jpg")

lcord=[ [0, 0, 500, 500]    ]
ll=imgcreate.create_images(img,lcord,100,300,8,0)

for gg in ll:
    print gg.shape
    cv2.imshow("hello",gg)
    cv2.waitKey(0)
cv2.imwrite("naoume.jpg", ll[0])
