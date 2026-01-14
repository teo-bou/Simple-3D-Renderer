import cv2
import numpy as np

WIDTH = 640
HEIGHT = 480

image = np.zeros((HEIGHT, WIDTH, 3))

cv2.imshow('Image', image)
cv2.waitKey(0)




