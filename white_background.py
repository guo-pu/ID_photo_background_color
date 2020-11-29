# 此程序名：white_background.py
# 作者：guo-pu
# 功能：把证件照的底色替换成白色
# 输入：证件照图片
# 输出：以白色为底色的证件照
# 编写时间：2020-11-22


import cv2
import numpy as np

# 读取照片
img=cv2.imread('test.jpg')

# 图像缩放——可选
# img = cv2.resize(img,None,fx=0.5,fy=0.5)

# 打印图片的信息————分辨率、图片通道
rows,cols,channels = img.shape
print(("图片分辨是：%s*%s  此图片是%s通道")%(rows,cols,channels))
cv2.imshow('img',img)

# 图片转换为灰度图
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)

# 图片的二值化处理
lower_blue=np.array([85,70,70]) #[85,70,70]
upper_blue=np.array([110,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)


# 先膨胀，再腐蚀
dilate=cv2.dilate(mask,None,iterations=3)
cv2.imshow('dilate',dilate)

erode=cv2.erode(dilate,None,iterations=4)
cv2.imshow('erode',erode)

# 遍历替换
for i in range(rows):
  for j in range(cols):
    if erode[i,j]==255:
      img[i,j]=(255,255,255) #白色底部--此处替换颜色，为BGR通道，不是RGB通道
cv2.imshow('res',img)

# 保存图片 可以以png、jpg、bmp方式保存，默认是以.png保存
s = cv2.imwrite('output_picture_white.png',img)
if s > 0:
  print("图片底色替换为白色，并保存成功！！")

# 其他格式保存图片：
# s = cv2.imwrite('output_picture2.jpg',img)
# s = cv2.imwrite('output_picture3.bmp',img)


# 键盘上按下q键退出
k = cv2.waitKey(0)
if k =='q':
  cv2.destroyAllWindows()

  
