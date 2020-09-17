The DJI Robomaster Objects in Context （DJI ROCO）

1、该文件中所有图像数据都是来自RoboMaster比赛直播数据，目前可提供的图像数据拍摄角度有限，仅作为参考和示例。

2、文件夹形式：
	image_annotation：目标检测标注文件，xml格式文件。标注文件格式和一般公开数据集的目标检测标注文件一致，文件里记录的是每个object在图像上的位置信息。

3、我们对图像上场地内的所有机器人、哨兵机器人和基地包括它们身上对应的所有装甲板都有标注。

     xml annotation文件解释：
	filename：对应图片的名字，内容是英文，可能和文件名不一致但并不影响使用。
	size：图像的width和height
	object的属性有：
		name：有5种属性值：car(机器人)，watcher（哨兵机器人），base（基地），ignore（忽略）, armor（装甲板）
			图片上出现的是一些由于反光导致的物体的影像、或者在场地外的机器人都标记为ignore。
		difficulty：表示物体的遮挡程度
			0：遮挡<=20%
			1，20%<遮挡<=50%
			2，遮挡>50%
		bendbox：表示每个目标物体的boundingbox坐标值。左上角坐标：(xmin，ymin)，右下角坐标：（xmax，ymax）, 所有坐标值都是基于1920x1080的原始图像而言
	armor的属性有：
   		armor_class: 装甲板上的数字id 。车是1-5，哨兵是6，基地是8，标记为none表示当前标注员肉眼分不清
   		armor_color：red红色、blue蓝色、gray灰色（装甲板不亮时的颜色分类）



1. Images in this file come from RoboMaster live data. Due to the limited camera angle, the available image data are for reference only.

2. Folder format:
	image Folder: files in .jpg
	image_annotation Folder: files in .xml. The format of annotation file is the same as the object detection annotation file in the general public dataset.
		                          The file records the position information of each object in the image.

3. We annotate robot, sentry, bases in the Battlefield and their corresponding armor plates on the image.
   Example of an xml annotation file：
	<filename> node: The correspongding picture name in English, which is fine to be inconsistent with the file name.
	<size> node: The width and height of the picture.
	<object> node has the following attributes:
		<name>: There are five attribute values:  car (robot), watcher (sentry), base, ignore, armor
			  Reflected image of objects or robots outside the Battlefiled will be annotated as ignore.
		<difficulty>: The degree of obscuration of the object
			0: Obscuration <= 20%
			1: 20%< Obscuration <=50%
			2: Obscuration >50%
		<bendbox>: Represents the boundingbox coordinates of each target object. The top left coordinates: (xmin, ymin), the bottom right coordinates: (xmax, ymax)
			     All coordinates are based on the original image of 1920x1080 pixels.
	<armor> node has the following attributes:
		<armor_class>: ID number of armor plate.  
			        ID number of cars are 1 to 5, watcher is 6 , base 8 and none means it's hard to identify.
		<armor_color>: Color of armor plate, including red, blue and gray. Gray indicates that the armor plate light is off.








