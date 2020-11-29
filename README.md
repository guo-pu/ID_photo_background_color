# 证件照背景颜色替换
证件照背景颜色替换；输入一张证件照，指定背景颜色，运行程序，自动替换证件照底色。


#### 1）把证件照的底色替换成红色
```shell
# 此程序名：red_background.py
# 作者：guo-pu
# 功能：把证件照的底色替换成红色
# 输入：证件照图片
# 输出：以红色为底色的证件照
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
dilate=cv2.dilate(mask,None,iterations=1)
cv2.imshow('dilate',dilate)

erode=cv2.erode(dilate,None,iterations=1)
cv2.imshow('erode',erode)

# 遍历替换
for i in range(rows):
  for j in range(cols):
    if erode[i,j]==255:
      img[i,j]=(0,0,255) #红色底部--此处替换颜色，为BGR通道，不是RGB通道
cv2.imshow('res',img)

# 保存图片 可以以png、jpg、bmp方式保存，默认是以.png保存
s = cv2.imwrite('output_picture_red.png', img)
if s > 0:
  print("图片底色替换为红色，并保存成功！！")

# 其他格式保存图片：
# s = cv2.imwrite('output_picture2.jpg',img)
# s = cv2.imwrite('output_picture3.bmp',img)


# 键盘上按下q键退出
k = cv2.waitKey(0)
if k =='q':
  cv2.destroyAllWindows()


```
执行如下命令运行程序：

```shell
python red_background.py
```
转换效果：

<img src="https://github.com/guo-pu/ID_photo_background_color/blob/master/%E8%BD%AC%E6%8D%A2%E6%95%88%E6%9E%9C%E5%9B%BE/%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%BA%A2%E8%89%B2%E5%BA%95%E5%9B%BE.png" /><br/>

#### 2）把证件照的底色替换成白色

```shell
python while_background.py
```
转换效果：

<img src="https://github.com/guo-pu/ID_photo_background_color/blob/master/%E8%BD%AC%E6%8D%A2%E6%95%88%E6%9E%9C%E5%9B%BE/%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%99%BD%E8%89%B2%E5%BA%95%E5%9B%BE.png" /><br/>

#### 3）把证件照的底色替换成蓝色

```shell
python blue_background.py
```

### 说明
测试图片来自百度图库：https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D6%A4%BC%FE%D5%D5%20%CD%BC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111
