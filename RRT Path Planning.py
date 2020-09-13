import cv2 as cv
import numpy as np
import random as rd
import RRT_Functions as rf

#------------------IMAGE READ & CONVERSION------------------------

#reading in photo file
img = cv.imread("Path Planning\spartan_logo.png",cv.IMREAD_UNCHANGED)
img_gray = cv.imread("Path Planning\spartan_logo.png",cv.IMREAD_GRAYSCALE)

#Desired size in pixels
width = 750
height = 750
size_des = (width, height)
img = cv.resize(img,size_des)
img_gray = cv.resize(img_gray,size_des)

#Convert grayscale image to black and white
thresh = 127
img_binary = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY)[1]

#---------------------PATH PLANNING------------------------------

#Path planning Start and End points
pt_start = [(0,0)]
pt_end = [(height-1,width-1)]
while True:
    pt_random = (rd.randint(0,height-1),rd.randint(0,width-1)) #create random point
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
    start_go = rf.NoGoCheck(line_start, img_binary)
    end_go = rf.NoGoCheck(line_end, img_binary)
    if start_go is True:
        pt_start.append(pt_random)
        start_line_point_start = (pt_start[point_start][1],pt_start[point_start][0])
        start_line_point_end = (pt_random[1],pt_random[0])
        img = cv.line(img,start_line_point_start,start_line_point_end,(0,0,0),2)
    if end_go is True:
        pt_end.append(pt_random)
        end_line_point_start = (pt_end[point_end][1],pt_end[point_end][0])
        end_line_point_end = (pt_random[1],pt_random[0])
        img = cv.line(img,end_line_point_start,end_line_point_end,(0,0,0),2)

    cv.imshow('Path Planning',img)
    print(start_go,end_go)
    if (start_go is True) and (end_go is True):
        print("SUCCESS!!!")
        cv.waitKey(0)
        #cv.destroyAllWindows()
        ##break 
    cv.waitKey(1)