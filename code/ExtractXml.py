import xml.dom.minidom
# D:\VS-Code-python\RM_DataProcess\robomaster_North China Regional Competition\image_annotation\追梦Vs追梦Team_BO3_2_0.xml
# D:\VS-Code-python\RM_DataProcess\robomaster_North China Regional Competition\image_annotation\SPRVsTOE_BO3_1_0.xml
# D:\VS-Code-python\RM_DataProcess\robomaster_North China Regional Competition\image_annotation\SPRVsTOE_BO5_3_0.xml
# D:\VS-Code-python\RM_DataProcess\robomaster_North China Regional Competition\image_annotation\TDTVsI Hiter_BO5_1_0.xml
index = [420, 386, 342, 222, 420, 295, 389]
filename = [r'\TDTVsI Hiter_BO5_4_{}', r'\追梦Vs追梦Team_BO3_2_{}', r'\SPRVsTOE_BO3_1_{}', r'\SPRVsTOE_BO5_3_{}',\
     r'\TDTVsI Hiter_BO5_1_{}', r'\TDTVsI Hiter_BO5_2_{}', r'\TDTVsI Hiter_BO5_3_{}']
dirPath = r'D:\VS-Code-python\RM_DataProcess\robomaster_North China Regional Competition'
annotationPath = dirPath + r'\image_annotation'
retPath = dirPath + r'\label'

'''
description:read xml file, return root
input:path of xml file
output:root node of xml file
'''
def readXml(filename):
    dom = xml.dom.minidom.parse(filename)
    root = dom.documentElement
    return root

'''
description:get tags using tagname
input:node; tagname
output:tags of the node
'''
def getElem(node, tagnames):
    elem = []
    for tagname in tagnames:
        elements = node.getElementsByTagName(tagname)
        if elements:
            elem.append(elements)
        else:
            elem.append([])
    return elem

'''
description:get data of tags
input:node
output:data
'''
def getData(nodes):
    data = []
    for node in nodes:
        nodeData = node.firstChild.data
        #print(nodeData)
        if nodeData:
            data.append(nodeData)
        else:
            data.append([])
    return data

'''
description:get the coordinates and the name of the bboxs
input:objectNode
output:bbox with name and coords
'''
def getBbox(nodes):
        
    objectTags = [getElem(objectNode, objectTagNames) for objectNode in nodes]
    # print(objectTags)

    # objectTag[0]:name; objectTag[1]:bbox
    bbox = [[getData(objectTag[0]), [getData(coord) for coord in getElem(objectTag[1][0], bboxTagNames)]] for objectTag in objectTags]
    #print(bbox)

    return bbox

'''
description：change bbox value into digital form
input:bbox
output:digital bbox
'''
def extractBbox(bbox):
    
    # convert name into digit number
    nameStr = bbox[0][0]
    # print(nameStr)

    if nameStr == 'car':
        nameDigit = 0
    elif nameStr == 'watcher':
        nameDigit = 1
    elif nameStr == 'base':
        nameDigit = 2
    elif nameStr == 'ignore':
        nameDigit = 3
    elif nameStr == 'armor':
        nameDigit = 4

    xmin, xmax, ymin, ymax = [float(coord[0]) for coord in bbox[1]]

    return [nameDigit, xmin, xmax, ymin, ymax]

'''
description:change the format of the bbox and normolization
input:bboxvalue:the old form of the bbox; size:the size of the picture
output:the needed form
'''
def changeBboxFormat(bboxValue, size):
    picHeight = float(size[0][0])
    picWidth = float(size[1][0])

    classDigit, xmin, xmax, ymin, ymax = bboxValue

    # deal with the abnormal data
    xmin = max(xmin, 0)
    ymin = max(ymin, 0)
    xmax = min(xmax, picWidth)
    ymax = min(ymax, picHeight)

    height = round((ymax - ymin)/picHeight, 3)
    width = round((xmax - xmin)/picWidth, 3)
    xCenter = round((xmax + xmin) / (2 * picWidth), 3)
    yCenter = round((ymin + ymax) / (2 * picHeight), 3)
    
    return [classDigit, xCenter, yCenter, width, height]

if __name__ == '__main__':
    
    annotationTagNames = ['filename', 'size', 'object']
    objectTagNames = ['name', 'bndbox']
    bboxTagNames = ['xmin', 'xmax', 'ymin', 'ymax']
    sizeTagNames = ['height', 'width']

    # for every patition
    for j in range(len(index)):

        # for every file
        for i in range(index[j]):
            fileName = (annotationPath + filename[j] + r'.xml').format(i)
            root = readXml(fileName)
            nodes = getElem(root, annotationTagNames)

            # pylint: disable=unbalanced-tuple-unpacking
            filenameNode, sizeNode, objectNodes = nodes
            # print(filenameNode, sizeNode, objectNodes)
            
            sizeElem = getElem(sizeNode[0], sizeTagNames)
            sizeData = [getData(it) for it in sizeElem]

            bboxs = getBbox(objectNodes)
            # print(bbox)

            for bbox in bboxs:
                bboxValues = extractBbox(bbox)
                # print(bboxValues)
                newBbox = changeBboxFormat(bboxValues, sizeData)
                # print(newBbox)
                with open((retPath + filename[j] + r'.txt').format(i), 'a', encoding='UTF-8') as f:
                    f.write(' '.join([str(it) for it in newBbox])+'\n')  
