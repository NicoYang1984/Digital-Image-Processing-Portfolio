from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#读入图像并转换为灰度图像
input_image = Image.open("input_rgb_image.jpg")
gray_image = input_image.convert("L")

# 将灰度图像转换为NumPy数组
gray_array = np.array(gray_image)
# print(gray_array)

# 计算灰度直方图
hist, bins = np.histogram(gray_array, bins=256, range=(0, 256))#参数解析：bins：直方图的柱子数量；range：灰度级别范围
#返回两个numpy数组：一个表示灰度值，另一个表示不同的灰度

# 计算归一化灰度直方图
normalized_hist = hist / float(np.sum(hist))

# 绘制灰度直方图
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.title("gray-scale histogram")
plt.xlabel("grayscale level")
plt.ylabel("pixel count")
plt.bar(bins[:-1], hist, width=1, color='gray', align='center')

# 绘制归一化灰度直方图
plt.subplot(122)
plt.title("Normalized grayscale histogram")
plt.xlabel("grayscale level")
plt.ylabel("normalized frequency")
plt.bar(bins[:-1], normalized_hist, width=1, color='gray', align='center')

plt.tight_layout()#自动调整布局，以显示在图形窗口中
plt.show()