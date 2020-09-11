import cv2 as cv
import numpy as np

#reading in photo file in the current folder
msu = cv.imread("spartan-helmet-og.png", cv.IMREAD_GRAYSCALE)

#slider variables
alpha_slider_max = 100
title_window = "Scaled Photo"

#track bar call back
def on_trackbar(val):
    alpha = val/alpha_slider_max
    width = int(msu.shape[1]*alpha)
    height = int(msu.shape[0]*alpha)
    dsize = (width, height)
    msu2 = cv.resize(msu, dsize)
    cv.imshow("msu", msu2)

cv.namedWindow(title_window)
trackbar_name = "Alpha x %d" % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window, 50, alpha_slider_max, on_trackbar)


#hold and terminate program
cv.waitKey(0) 
cv.destroyAllWindows()


#Path planning
pt_start = 1
pt_end = 1
pt_current = 1
