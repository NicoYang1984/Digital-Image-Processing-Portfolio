from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# 读取RGB图像
input_image = Image.open("input_rgb_image.jpg")#读入图像

# 显示原始RGB图像
plt.figure(figsize=(12, 4))#创建新的图形窗口，大小：宽度为12英寸，高度为4英寸
plt.subplot(131)#在窗口中创建子图：(131)中的1表示总行数，3表示总列数，1表示当前子图的位置。
plt.title("RGB Image")#当前子图标题
plt.imshow(input_image)
plt.axis('off')#不显示坐标轴

# 将图像转换为灰度图像
gray_image = input_image.convert("L")

#显示灰度图像
plt.subplot(132)
plt.title("Gray Image")#当前子图标题
plt.imshow(gray_image, cmap='gray')#告诉matplotlib使用灰度颜色映射来显示图像，否则可能会选择其他颜色映射
plt.axis('off')

# 将图像进行二值化处理
threshold = 128  # 二值化的阈值，改变其大小会得到不同的结果
binary_image = gray_image.point(lambda p: p > threshold and 255)#使用lambda表达式确定阈值

#显示二值化图像
plt.subplot(133)
plt.title("Binary Image")
plt.imshow(binary_image, cmap='gray')
plt.axis('off')

# 展示图像
plt.tight_layout()
plt.show()