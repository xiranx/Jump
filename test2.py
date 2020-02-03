import cv2
import numpy as np

class Getoutofloop(Exception):
    pass

def CalculateCenter(screenshot):
    (row,column,channel)=screenshot.shape
    rough_distance = 70
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
                if screenshot[i,j][0]<130 and screenshot[i,j][0]>80 and screenshot[i,j][1]<100 and screenshot[i,j][2]<100:
                    print(screenshot[i,j])
                    start = [i+95,j-4]
                    raise Getoutofloop()
    except Getoutofloop:
        pass
    print (start)
    return start


screenshot = cv2.imread('/Users/xxr/Desktop/xrr_screenshot/autojump.png')
(row,column,channel)=screenshot.shape
screenshot = cv2.resize(screenshot,(int(column*0.5),int(row*0.5)))
#CalculateCenter(screenshot)
StartCenter(screenshot)
#print(((147-219)**2+(224-208)**2+(196-205)**2)**0.5)
