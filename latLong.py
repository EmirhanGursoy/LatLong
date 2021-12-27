import numpy as np
import cv2 as cv
img = cv.imread('kirmiziAlan.png',0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#1 pixel(X) = 0.0002645833 m
a = cx * 0.0002645833
b = cy * 0.0002645833
c = 40.996207
d = 29.060491
print("Kırmızı alanın merkezi(x,y): {} , {}".format(a,b))

h = (a**2 + b**2) ** 0.5
e = (c**2 + d**2) ** 0.5


