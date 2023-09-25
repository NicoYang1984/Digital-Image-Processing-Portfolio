import cv2
import numpy as np
import matplotlib.pyplot as plt

#用CV库读取图像
image = cv2.imread("input_rgb_image.jpg")




# 定义对比度拉伸的参数
min_intensity = 0
max_intensity = 255
min_input = 0
max_input = 255
min_output = 100
max_output = 150

#增加图形亮度的参数：可以用加法也可以用乘法
def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#将输入图像转换为HSV空间：色相（Hue）、饱和度（Saturation）和明度（Value）。
    hsv[:, :, 0] = hsv[:, :, 0]
    hsv[:, :, 1] = hsv[:, :, 1]
    hsv[:, :, 2] = np.clip(hsv[:, :, 2]*value, 0, 255)#在明度通道中为每个值加50，其中clip表示切片：限定取值范围为0到255
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return result

def decrease_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0] = hsv[:, :, 0]
    hsv[:, :, 1] = hsv[:, :, 1]
    hsv[:, :, 2] = np.clip(hsv[:, :, 2]/value, 0, 255)
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return result

#变亮区间内部
def increase_interval_brightness(img, value, left, right):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    v_channel = hsv[:, :, 2]#获取明度通道
    v_channel[(v_channel >= left) & (v_channel <= right)] *= np.uint8(value) #对满足条件的像素进行点乘操作。其中下标处放布尔代数式表示布尔索引操作。对满足布尔代数式的下标进行操作

    hsv[:, :, 2] = np.clip(v_channel, 0, 255)  # 在明度通道中为每个值加50，其中clip表示切片：0到255
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return result


# 显示原始图像、增加亮度后的图像和减少亮度后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Brightened Image', increase_brightness(image, 2))
cv2.imshow('Darkened Image', decrease_brightness(image, 2))
cv2.imshow('Brightened-interval Image', increase_interval_brightness(image, 2, 100, 150))
cv2.waitKey(0)#等待用户下一个按键。0表示任意按键
cv2.destroyAllWindows()#销毁所有窗口
# plt.subplot(221)#在窗口中创建子图：(131)中的1表示总行数，3表示总列数，1表示当前子图的位置。
# plt.title("Original Image")#当前子图标题
# plt.imshow(image)
# plt.axis('off')#不显示坐标轴
# plt.subplot(222)#在窗口中创建子图：(131)中的1表示总行数，3表示总列数，1表示当前子图的位置。
# plt.title("Brightened Image")#当前子图标题
# plt.imshow(increase_brightness(image, 35))
# plt.axis('off')#不显示坐标轴
#
# plt.tight_layout()
# plt.show()