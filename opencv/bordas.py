import cv2
import matplotlib.pyplot as plt
import numpy as np

PATH = "./kurisu.jpg"

# Grey filter
img = cv2.cvtColor(cv2.imread(PATH), cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

imagens = [img, img_gray]

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

for i in range(2):
    if len(imagens[i].shape) == 2:
        axes[i].imshow(imagens[i], cmap='gray')
    else:
        axes[i].imshow(imagens[i])

    # axes[i].axis('off')

plt.show(block=False)
plt.pause(1)
plt.close()

# Blur
img_blur = cv2.blur(img, (10,10))
plt.imshow(img_blur)

plt.show(block=False)
plt.pause(1)
plt.close()

# Borders
img_laplacian = cv2.Laplacian(img, cv2.CV_8U, 5)
plt.imshow(img_laplacian, cmap="gray")
plt.show()
