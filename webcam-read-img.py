import cv2

img = cv2.imread('C:/Users/erhicakorf/Documents/Specno/FaceDetection/saved_img.png')
 
cv2.imshow('sample image',img)
 
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image