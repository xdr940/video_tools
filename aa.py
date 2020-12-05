import cv2
import matplotlib.pyplot as plt
#np = cv2.imread("/home/roit/Desktop/color/000001.tga",cv2.IMREAD_GRAYSCALE)
np = cv2.imread("./depth/00020.jpg",cv2.CAP_MODE_RGB)

plt.imshow(np)
plt.show()
print('ok')