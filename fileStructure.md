The DJI Robomaster Objects in Context ��DJI ROCO��

1�����ļ�������ͼ�����ݶ�������RoboMaster����ֱ�����ݣ�Ŀǰ���ṩ��ͼ����������Ƕ����ޣ�����Ϊ�ο���ʾ����

2���ļ�����ʽ��
	image_annotation��Ŀ�����ע�ļ���xml��ʽ�ļ�����ע�ļ���ʽ��һ�㹫�����ݼ���Ŀ�����ע�ļ�һ�£��ļ����¼����ÿ��object��ͼ���ϵ�λ����Ϣ��

3�����Ƕ�ͼ���ϳ����ڵ����л����ˡ��ڱ������˺ͻ��ذ����������϶�Ӧ������װ�װ嶼�б�ע��

     xml annotation�ļ����ͣ�
	filename����ӦͼƬ�����֣�������Ӣ�ģ����ܺ��ļ�����һ�µ�����Ӱ��ʹ�á�
	size��ͼ���width��height
	object�������У�
		name����5������ֵ��car(������)��watcher���ڱ������ˣ���base�����أ���ignore�����ԣ�, armor��װ�װ壩
			ͼƬ�ϳ��ֵ���һЩ���ڷ��⵼�µ������Ӱ�񡢻����ڳ�����Ļ����˶����Ϊignore��
		difficulty����ʾ������ڵ��̶�
			0���ڵ�<=20%
			1��20%<�ڵ�<=50%
			2���ڵ�>50%
		bendbox����ʾÿ��Ŀ�������boundingbox����ֵ�����Ͻ����꣺(xmin��ymin)�����½����꣺��xmax��ymax��, ��������ֵ���ǻ���1920x1080��ԭʼͼ�����
	armor�������У�
   		armor_class: װ�װ��ϵ�����id ������1-5���ڱ���6��������8�����Ϊnone��ʾ��ǰ��עԱ���۷ֲ���
   		armor_color��red��ɫ��blue��ɫ��gray��ɫ��װ�װ岻��ʱ����ɫ���ࣩ



1. Images in this file come from RoboMaster live data. Due to the limited camera angle, the available image data are for reference only.

2. Folder format:
	image Folder: files in .jpg
	image_annotation Folder: files in .xml. The format of annotation file is the same as the object detection annotation file in the general public dataset.
		                          The file records the position information of each object in the image.

3. We annotate robot, sentry, bases in the Battlefield and their corresponding armor plates on the image.
   Example of an xml annotation file��
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








