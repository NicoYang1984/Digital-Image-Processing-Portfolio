import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input_rgb_image.jpg", cv2.IMREAD_GRAYSCALE)#cv2.imread_GRAYSCALE指定输入图像为灰度图像

#调用函数进行直方图均衡化。Hist表示histogram。
equalized_image = cv2.equalizeHist(image)
# normalized_image = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(image)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
normalized_image = clahe.apply(image)

# 绘制直方图
plt.figure(figsize=(12, 6))

# 原始图像直方图
plt.subplot(2, 2, 1)
plt.hist(image.ravel(), bins=256, range=(0, 256), color='gray', alpha=0.7)
plt.title('Original Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# 直方图均衡化后的直方图
plt.subplot(2, 2, 2)
plt.hist(equalized_image.ravel(), bins=256, range=(0, 256), color='gray', alpha=0.7)
plt.title('Equalized Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# 规定化后的直方图
plt.subplot(2, 2, 3)
plt.hist(normalized_image.ravel(), bins=256, range=(0, 256), color='gray', alpha=0.7)
plt.title('Normalized Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# 显示图像和直方图
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.tight_layout()
plt.show()

#显示规定化和均衡化之后的图像
cv2.imshow('Equalized Image', equalized_image)
cv2.imshow('Normalized Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()