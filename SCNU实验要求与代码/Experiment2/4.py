import cv2
import numpy as np

image = cv2.imread("input_rgb_image.jpg")

mean = 0
stddev = 0.64


noise = np.random.normal(mean, stddev, image.shape).astype(np.uint8)#创建高斯噪声
noisy_image = cv2.add(noise, image)#将原图和噪声矩阵相加


cv2.imshow("noisy_image", noisy_image)
cv2.imshow("denoised_image_with_GaussianBlur", cv2.GaussianBlur(noisy_image, (5,5), 0))#使用高斯滤波去噪
cv2.imshow("denoised_image_with_MedianBlur", cv2.medianBlur(noisy_image, 5))#使用中值滤波，5表示卷积核大小
cv2.imshow("denoised_image_with_bilateralFilter",cv2.bilateralFilter(noisy_image, 9, 75, 75))#使用双边滤波去噪。其中9表示卷积核的直径，75表示颜色空间标准差和坐标空间标准差
cv2.waitKey(0)#注意K大写
cv2.destroyAllWindows()

