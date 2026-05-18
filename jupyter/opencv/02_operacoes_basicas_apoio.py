import cv2

def redimensiona_img(img, scale=0.5):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

img_vi = cv2.imread("assets/vi.jpg")
cv2.imshow("Vi - Arcane", redimensiona_img(img_vi, 0.25))
cv2.waitKey() 