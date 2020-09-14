import cv2 as cv
import numpy as np
import random as rd
import RRT_Functions as rf

#------------------IMAGE READ & CONVERSION------------------------

#reading in photo file
img = cv.imread("Path Planning\spartan_logo.png",cv.IMREAD_UNCHANGED)
img_gray = cv.imread("Path Planning\spartan_logo.png",cv.IMREAD_GRAYSCALE)

#Desired size in pixels
width = 250
height = 250
delta = round(min(width,height)*0.1)
size_des = (width, height)
img = cv.resize(img,size_des)
img_gray = cv.resize(img_gray,size_des)

#Convert grayscale image to black and white
thresh = 127
img_binary = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY)[1]

#---------------------PATH PLANNING------------------------------

#Path planning Start and End points
pt_start = [(9,9)]
cv.circle(img,pt_start[0],10,(0,255,0),-1)
pt_end = [(height-11,width-11)]
cv.circle(img,pt_end[0],10,(0,0,255),-1)
success = False
counter = 0
loop = 0
while True:
    loop+=1
    pt_random = (rd.randint(0,height-1),rd.randint(0,width-1)) #create random point
    if (pt_random in pt_start) or (pt_random in pt_end):continue
    else:
        if loop%5 == 0: pt_random = (round((pt_start[len(pt_start)-1][0]+pt_end[len(pt_end)-1][0])/2),round((pt_start[len(pt_start)-1][1]+pt_end[len(pt_end)-1][1])/2))
        #find closest starting point
        point_start = rf.DistCheck(pt_start, pt_random)
        point_end = rf.DistCheck(pt_end, pt_random)
        #create a list of line points
        line_start = rf.LineGen(pt_start[point_start],pt_random,delta)
        line_end = rf.LineGen(pt_end[point_end],pt_random,delta)
    #check if line intersects no go region
    start_go = rf.NoGoCheck(line_start, img_binary)
    end_go = rf.NoGoCheck(line_end, img_binary)
    if start_go is True:
        pt_start.append(line_start[len(line_start)-1])
        start_line_point_start = (pt_start[point_start][1],pt_start[point_start][0])
        start_line_point_end = (line_start[len(line_start)-1][1],line_start[len(line_start)-1][0])
        img = cv.line(img,start_line_point_start,start_line_point_end,(0,0,0),3)
        counter+=1
    if end_go is True:
        pt_end.append(line_end[len(line_end)-1])
        end_line_point_start = (pt_end[point_end][1],pt_end[point_end][0])
        end_line_point_end = (line_end[len(line_end)-1][1],line_end[len(line_end)-1][0])
        img = cv.line(img,end_line_point_start,end_line_point_end,(0,0,0),3)
        counter+=1
    if (end_go is True) or (start_go is True):
                connect = rf.LineGen(pt_start[len(pt_start)-1],pt_end[len(pt_end)-1],max(width,height))
                finish = rf.NoGoCheck(connect, img_binary)
                if finish is True:
                    cv.line(img,(pt_start[len(pt_start)-1][1],pt_start[len(pt_start)-1][0]),(pt_end[len(pt_end)-1][1],pt_end[len(pt_end)-1][0]),(0,0,0),2)
                    print("Super Success!!")
                    success = True
                    counter+=1
    cv.imshow('Path Planning',img)
    if (success is True) or line_start[len(line_start)-1] == line_end[len(line_end)-1] and start_go is True and end_go is True:
        print(counter)
        cv.waitKey(0)
        cv.destroyAllWindows()
        break 
    cv.waitKey(1)