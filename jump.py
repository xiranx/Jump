import cv2
import numpy as np
import os
from threading import Timer
import time

class Getoutofloop(Exception):
    pass

def CalculateCenter(screenshot):
    (row,column,channel)=screenshot.shape
    rough_distance = 40
    coor=[]
    top = False
    right = False
    right_candidate = []
    try:
        for x in range(150,row,1):
            for y in range(column-1,0,-1):
                distance = 0
                for i in range(3):
                    if screenshot[x,y][i]>screenshot[x,y-1][i]:
                        distance = distance+screenshot[x,y][i]-screenshot[x,y-1][i]
                    else:
                        distance = distance+screenshot[x,y-1][i]-screenshot[x,y][i]
                if distance>=rough_distance:
                    if top==False:
                        coor.append([x,y-1])
                        top=True
                    else:
                        right_candidate.append([x,y-1])
                        if len(right_candidate)>2 and right_candidate[len(right_candidate)-1][1]<=right_candidate[len(right_candidate)-2][1] and right_candidate[len(right_candidate)-2][1]>= right_candidate[len(right_candidate)-3][1]:
                            coor.append(right_candidate[len(right_candidate)-2])
                            right = True
                    if right:
                        print(1)
                        print(coor)
                        raise Getoutofloop()
                    break
    except Getoutofloop:
        pass
    center = [coor[1][0],coor[0][1]]
    print(center)
    return center

def StartCenter(screenshot):
    (row,column,channel) = screenshot.shape
    try:
         for i in range(150,row,1):
            for j in range(0,column,1):
                if 70<screenshot[i,j][0]<100 and 50<screenshot[i,j][1]<60 and screenshot[i,j][2]<60:
                    print(screenshot[i,j])
                    start = [i+95,j-4]
                    raise Getoutofloop()
    except Getoutofloop:
        pass
    print (start)
    return start

def Distance(start,center):
    distance1 = (center[0]-start[0])**2+(center[1]-start[1])**2
    distance = distance1**0.5
    return distance

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png /Users/xxr/Desktop/xrr_screenshot')

def jump(distance):
    press_time = distance*2.5
    press_time = int(press_time)
    cmd = 'adb shell input swipe 320 410 320 410 ' + str(press_time)
    os.system(cmd)


def task():
    pull_screenshot()
    screenshot = cv2.imread('/Users/xxr/Desktop/xrr_screenshot/autojump.png')
    (row,column,channel)=screenshot.shape
    screenshot = cv2.resize(screenshot,(int(column*0.5),int(row*0.5)))
    center = CalculateCenter(screenshot)
    start = StartCenter(screenshot)
    distance = Distance(start,center)
    jump(distance)

if __name__=="__main__":
    while True:
        task()
        time.sleep(0.4)


