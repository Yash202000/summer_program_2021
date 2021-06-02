"""
Task 4.3
Take 2 image and combine it to form single image. For example collage 
"""

# Here we can use np.vstack and np.hstack ig this will be better approach. to use vstack and hstack if 
# image dimension is same

# t=np.concatenate((img1,img2),1)
def concateHorizontally(img1,img2):
    t=np.hstack((img1,img2))
    return t

# t=np.concatenate((img1,img2),0)
def concateVertically(img1,img2):
    t=np.vstack((img1,img2))
    return t


def printImg(temp1):
    cv2.imshow('img1',temp1)
    cv2.waitKey()
    cv2.destroyAllWindows()
  
t=concateHorizontally(crp1,crp2)
printImg(t)
