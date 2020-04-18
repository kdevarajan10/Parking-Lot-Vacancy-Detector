import cv2
import os
import xml.etree.ElementTree as ET
import glob

ctr = 1
for filename in glob.glob('E:\\HW1\\cv-homework-3-kdevarajan10\\Parking_images\\*\\sunny\\*\\*.xml', recursive=True):

    tree = ET.parse(filename)
    root = tree.getroot()

    coordinates = dict()

    for space in root.findall('space'):
        id = space.get('id')
        occupied = space.get('occupied')
        if occupied == '1':
            coordinates[id] = []
            for point in space.iter('point'):
                x = point.attrib.get('x')
                y = point.attrib.get('y')
                coordinates[id].append((x, y))

    coordinates = {int(i): j for i, j in coordinates.items()}
    # print(coordinates)

    imgname = os.path.splitext(filename)[0] + ".jpg"
    img = cv2.imread(imgname)

    for i in coordinates.keys():
        x1 = [int(p) for (p, q) in coordinates[i]]
        y1 = [int(q) for (p, q) in coordinates[i]]
        xmin = min(x1)
        ymin = min(y1)
        xmax = max(x1)
        ymax = max(y1)
        crop_img = img[ymin - 10:ymax + 10, xmin - 10:xmax + 10]
        cv2.imwrite("E:\\HW1\\cv-homework-3-kdevarajan10\\positive_images\\pos_img" + str(ctr) + ".jpg", crop_img)
        ctr = ctr + 1