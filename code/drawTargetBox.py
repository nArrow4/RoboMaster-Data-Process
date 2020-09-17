from cv2 import cv2
import sys
import os

class_ = {'car':0, "watcher":1, "base":2, "ignore":3, "armor":4}

'''
despcription: draw box and write text on the img, except for class 'ignore'. 
param: box
return: None
'''
def drawBox(box):

    xCenter, yCenter, width, height = resizeToOrigin(box)
    if xCenter != -1:
        cv2.rectangle(img, (int(xCenter-width/2), int(yCenter-height/2)), (int(xCenter+width/2), int(yCenter+height/2)), (0, 0, 255))
        targetClassStr = list(class_.keys())[int(box[0])]
        cv2.putText(img, targetClassStr, ((int(xCenter-width/2), int(yCenter-height/2))), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255))

'''
despcription: resize the box into its origin size 
param: box
return: YOLO style box
'''
def resizeToOrigin(box):
    targetClassDigit, xCenter, yCenter, width, height = box
    
    if targetClassDigit == 3:
        return (-1, -1, -1, -1)
    else:
        xCenter *= picWidth
        yCenter *= picHeight
        width *= picWidth
        height *= picHeight
        # print(xCenter, yCenter, width, height)
    return (xCenter, yCenter, width, height)

if __name__ == '__main__':
    cur_dir = sys.path[0]
    dataPath = os.path.join(cur_dir, '../robomaster_North China Regional Competition/images')
    
    files = os.listdir(dataPath)
    for filePath in files:

        if '.jpg' in filePath:
            picPath = os.path.join(dataPath, filePath)
            boxPath = picPath[:-4] + '.txt'
            # print(picPath, boxPath)
            
            img = cv2.imread(picPath)
            cv2.imshow('img', img)
            picHeight, picWidth, _ = img.shape

            with open(boxPath, 'r', encoding='UTF-8') as f:
                boxes = f.readlines()
                for box in boxes:
                    box_ = list(map(float, box.strip('\n').split()))
                    drawBox(box_)
                cv2.imshow('LabeledImg', img)
                cv2.imwrite(os.path.join(dataPath, '../LabeledImg/', filePath[:-4]+'_labeled.jpg'), img)
            cv2.waitKey(0)
            