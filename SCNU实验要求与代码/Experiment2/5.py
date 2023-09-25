import cv2
from scipy.ndimage import convolve
import numpy as np

image = cv2.imread("input_rgb_image.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#由于拉普拉斯算子只能处理单通道图像，所以要把原图像转换成灰度图像来处理

#定义不同的拉普拉斯算子核进行优化
laplacian_kernel_1 = np.array([[0,-1,0],
                            [-1,4,-1],
                            [0,-1,0]], dtype=np.float32)#使用np.array函数进行算子定义
laplacian_kernel_2 = np.array([[-1,-1,-1],
                            [-1,8,-1],
                            [-1,-1,-1]], dtype=np.float32)#定义数据类型都要用np(如np.uint8)
cv2.imshow("Original_Image", gray_image)
cv2.imshow("Laplacian_Processed_Image1", convolve(gray_image,laplacian_kernel_1))#使用convolve对图像进行卷积操作
cv2.imshow("Laplacian_Processed_Image2", convolve(gray_image,laplacian_kernel_2))
cv2.waitKey(0)#注意K大写
cv2.destroyAllWindows()