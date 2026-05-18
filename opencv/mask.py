import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.cvtColor(cv2.imread("./kurisu.jpg"), cv2.COLOR_BGR2RGB)
mask = cv2.rectangle(np.zeros_like(img), (100, 100), (330, 350), (255, 255, 255), thickness=cv2.FILLED)
masked_img = cv2.bitwise_and(img, mask)
plt.imshow(masked_img)
plt.show()
