import cv2 as cv
import numpy as np
import random as rd
import RRT_Functions as rf

#------------------IMAGE READ & CONVERSION------------------------

#reading in photo file
img = cv.imread("Path Planning\spartan-helmet-og.png",cv.IMREAD_UNCHANGED)
img_gray = cv.imread("Path Planning\spartan-helmet-og.png",cv.IMREAD_GRAYSCALE)

#Desired size in pixels
width = 500
height = 500
size_des = (width,height)
img = cv.resize(img,size_des)
img_gray = cv.resize(img_gray,size_des)

#Convert grayscale image to black and white
thresh = 127
img_binary = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY)[1]


#---------------------PATH PLANNING------------------------------

#Path planning Start and End points
pt_start = [(0,0)]
pt_end = [(width-1,height-1)]
while True:
    pt_random = (rd.randint(0,width-1),rd.randint(0,height-1)) #create random point
    if (pt_random in pt_start) or (pt_random in pt_end):
        continue
    else:
        #find closest starting point
        point_start = rf.DistCheck(pt_start, pt_random)
        point_end = rf.DistCheck(pt_end, pt_random)
        #create a list of line points
        line_start = rf.LineGen(pt_start[point_start],pt_random)
        line_end = rf.LineGen(pt_end[point_end],pt_random)
    #check if line intersects no go region
    start_go = rf.NoGoCheck(line_start, img_binary, img)
    end_go = rf.NoGoCheck(line_end, img_binary, img)
    if start_go is True:
        pt_start.append(pt_random)
        img = cv.line(img,pt_start[point_start],pt_random,(0,0,0),1)
    if end_go is True:
        pt_end.append(pt_random)
        img = cv.line(img,pt_end[point_end],pt_random,(0,0,0),1)

    cv.imshow('Path Planning',img)
    print(start_go,end_go)
    ret_key = cv.waitKey(-1)
    if ret_key == ord('q'):
        cv.destroyAllWindows() 
        break
    elif ret_key == ord('n'):
        continue