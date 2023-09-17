import cv2
import matplotlib.pyplot as plt

# 读取第一幅图像
image1 = cv2.imread("image1.jpg")

# 读取第二幅图像
image2 = cv2.imread("image2.jpg")

#用addWeighted进行加权图像相加。0表示不增加图像的亮度
result_image = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

# 转换BGR颜色通道为RGB，以便matplotlib正确显示
result_image_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

#展示相加前后图片
plt.figure(figsize=(12, 4))#创建新的图形窗口，大小：宽度为12英寸，高度为4英寸
plt.subplot(131)
plt.title("image1")
plt.imshow(image1, cmap='viridis')
plt.axis('off')
plt.subplot(132)
plt.title("image2")
plt.imshow(image2, cmap='viridis')
plt.axis('off')
plt.subplot(133)
plt.title("result image")
plt.imshow(result_image_rgb)
plt.axis('off')

plt.tight_layout()#自动调整布局，以显示在图形窗口中
plt.show()


