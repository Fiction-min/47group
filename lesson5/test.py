import cv2
import numpy as np

img = cv2.imread('cutimg.jpg.')
cv2.imshow('image1', img)

# 将图像转为灰度图
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image2', img)


# 反色
def inverse_color(edged):
    height, width = edged.shape
    img2 = edged.copy()
    for i in range(height):
        for j in range(width):
            img2[i, j] = (255 - edged[i, j])
    return img2


cv2.imshow('image3', inverse_color(img))

# 水平投影
ret, thresh1 = cv2.threshold(inverse_color(img), 130, 255, cv2.THRESH_BINARY)
cv2.imshow('image4', thresh1)
image = thresh1.copy()
(h, w) = thresh1.shape  # 返回高和宽
# 初始化一个跟图像高一样长度的数组，用于记录每一行的黑点个数
a = [0 for z in range(0, h)]
for j in range(0, h):  # 遍历每一行
    for i in range(0, w):  # 遍历每一列
        if thresh1[j, i] == 0:  # 判断该点是否为黑点，0代表黑点
            a[j] += 1  # 该行的计数器加一
            thresh1[j, i] = 255  # 将其改为白点，即等于255

for j in range(0, h):  # 遍历每一行
    for i in range(0, a[j]):  # 从该行应该变黑的最左边的点开始向最右边的点设置黑点
        thresh1[j, i] = 0  # 设置黑点
cv2.imshow('image5', thresh1)

# 垂直投影
ret, thresh1 = cv2.threshold(inverse_color(img), 130, 255, cv2.THRESH_BINARY)
(h, w) = thresh1.shape  # 返回高和宽
# 初始化一个跟图像宽一样长度的数组，用于记录每一列的黑点个数
a = [0 for z in range(0, w)]
for j in range(0, w):  # 遍历每一列
    for i in range(0, h):  # 遍历每一行
        if thresh1[i, j] == 0:  # 判断该点是否为黑点，0代表是黑点
            a[j] += 1  # 该列的计数器加1
            thresh1[i, j] = 255  # 记录完后将其变为白色，即等于255

for j in range(0, w):  # 遍历每一列
    for i in range(h - a[j], h):  # 从该列应该变黑的最顶部的开始向最底部设为黑点
        # for i in range(0,a[i]):
        thresh1[i, j] = 0  # 设为黑点
cv2.imshow('image6', thresh1)

# 矩形分割字符
image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
red = (0, 0, 255)
# 设置矩形的各参数
cv2.rectangle(image, (10, 10), (65, 120), red, 2)
cv2.rectangle(image, (75, 10), (135, 120), red, 2)
cv2.rectangle(image, (160, 10), (220, 120), red, 2)
cv2.rectangle(image, (225, 10), (290, 120), red, 2)
cv2.rectangle(image, (300, 10), (355, 120), red, 2)
cv2.rectangle(image, (360, 10), (415, 120), red, 2)
cv2.rectangle(image, (420, 10), (480, 120), red, 2)
cv2.imshow('image7', image)
cv2.waitKey(0)