import cv2
import numpy as np

#设置区间外的灰度值为低值
def low_grayscale_image(img,lower_limit,upper_limit,value):
    return np.where((img >= lower_limit) & (img <= upper_limit), img, value)

# 设置区间外的灰度值为零值
def zero_grayscale_image(img, lower_limit, upper_limit):
    # mask = np.where((img >= lower_limit) & (img <= upper_limit), 1,0)#设置布尔掩码，将满足区间的像素值置1，其余置0。其中np.where为生成掩码的工具
    # result = (img * mask).astype(np.uint8)#修改数据类型为uint8（用float也可以）来保证图片的正常显示
    # result = np.where((img >= lower_limit) & (img <= upper_limit), img, 0)  # 代码优化1.0：其中img表示原值
    return np.where((img >= lower_limit) & (img <= upper_limit), img, 0)#代码优化2.0：将其单独整合到输出当中


#读入图像并转换为灰度图像
# input_image = Image.open("input_rgb_image.jpg")#注意用不同的库读取图片会生成不一样的数据类型
image = cv2.imread("input_rgb_image.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original_Image", gray_image)
cv2.imshow("zero_grayscale_image", zero_grayscale_image(gray_image, 80, 150))
cv2.imshow("low_grayscale_image", low_grayscale_image(gray_image, 80, 150, 50))
cv2.waitKey(0)#注意K大写
cv2.destroyAllWindows()


