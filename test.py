import cv2
import numpy as np
screenshot = cv2.imread('/Users/xxr/Desktop/xrr_screenshot/autojump.png')
(row,column,channel) = screenshot.shape
screenshot = cv2.resize(screenshot,(int(column*0.5),int(row*0.5)))
#screenshot[580,135]=255
screenshot[431, 519]=0
screenshot[570, 203]=255
print(screenshot[460:470,170])
cv2.imshow("cheng",screenshot)
cv2.waitKey()

