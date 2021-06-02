"""
Task 4.1
Create image by yourself Using Python Code.
"""
import cv2
import numpy as np

def printImg(temp1):
    cv2.imshow('img1',temp1)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
l = np.zeros((500,600))
l[60:120,120:180]=1
l[60:120,600-180:600-120]=1
l[220:280,270:320]=1
l[340:380,140:470]=1
l[10:12]=1
l[-12:-10]=1
l[:,10:12]=1
l[:,-12:-10]=1
printImg(l)
