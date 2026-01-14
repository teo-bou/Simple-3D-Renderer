import cv2
import numpy as np

WIDTH = 640
HEIGHT = 480


def square(image, x0, y0, x1, y1):
    for x in range(x0, x1):
        for y in range(y0, y1):
            image[y%HEIGHT, x%WIDTH] = (1, 0, 0)
    return image

for i in range(1000):
    image = np.zeros((HEIGHT, WIDTH, 3))
   


    image = square(image, i, i, 400+i, 400+i)

    cv2.imshow('Image', image)
    cv2.waitKey(10)




