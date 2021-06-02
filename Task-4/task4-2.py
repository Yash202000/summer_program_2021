# Code to swap 2nd image content to 1st image with provided dimension....
"""
Task 4.2
Take 2 image crop some part of both image and swap it. 
"""
import cv2

def swapcrop2inImg1(img1_path,img2_path,dim=(0,0,0,0)):                
    img1=cv2.imread(img1_path)
    img2=cv2.imread(img2_path)
    img1[dim[0]:dim[1],dim[2]:dim[3]],img2[dim[0]:dim[1],dim[2]:dim[3]]=img2[dim[0]:dim[1],dim[2]:dim[3]],img1[dim[0]:dim[1],dim[2]:dim[3]]
    return img1

def printImg(temp1):
    cv2.imshow('img1',temp1)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
temp1=swapcrop2inImg1("image1.png","image2.png",(200,600,300,800))
printImg(temp1)
