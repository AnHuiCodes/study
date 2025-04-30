import cv2
import numpy as np

# 读取图片
image = cv2.imread('img.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 这里需要手动或自动地标记出水印的位置
# 假设我们有一个水印的掩码（mask），其中水印区域为白色（255），其余为黑色（0）
# 注意：这里我们仅作为示例手动创建一个简单的掩码
# 在实际应用中，你可能需要使用图像分割、边缘检测等技术来生成掩码
mask = np.zeros(gray.shape, dtype=np.uint8)
# 假设水印位于图像的中心部分，我们手动绘制一个矩形作为掩码
cv2.rectangle(mask, (100, 100), (200, 200), 255, -1)

# 使用inpaint函数去除水印
# 3是inpaint算法的inpaintRadius，它决定了算法考虑周围像素的范围
dst = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

# 显示结果
cv2.imshow('Original', image)
cv2.imshow('Mask', mask)
cv2.imshow('Inpainted', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果
cv2.imwrite('result.png', dst)
