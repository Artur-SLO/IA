import cv2
import numpy as np

obama_img = cv2.imread("assets/obama.jpg")
cv2.imshow("Obama", obama_img)

# Blurring
# kernel = np.ones([3,3], dtype=np.float32)
# kernel = kernel / kernel.sum()
# obama_filt = cv2.filter2D(src=obama_img, ddepth=-1, kernel=kernel)
# cv2.imshow("Obama filt", obama_filt)

# Sharpening
# kernel = np.ones([3,3], dtype=np.float32)
# kernel[1,1] = -7
kernel = np.array([
                    [-1,-1,-1,-1,-1],
                    [-1, 2, 2, 2,-1],
                    [-1, 2, 8, 2,-1],
                    [-1, 2, 2, 2,-1],
                    [-1,-1,-1,-1,-1]
                  ])
kernel = kernel / kernel.sum()
obama_sharp = cv2.filter2D(src=obama_img, ddepth=-1, kernel=kernel)
cv2.imshow("Obama sharp", obama_sharp)


cv2.waitKey(0) 
