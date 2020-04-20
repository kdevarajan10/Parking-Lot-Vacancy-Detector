import cv2
import glob
import os
f = open("info1.dat", 'w')

for filename in glob.glob('positive_images\\*.jpg'):
    img_name = os.path.basename(filename)
    img = cv2.imread(filename)
    h = img.shape[0]
    w = img.shape[1]

    f.write(img_name + " 1 0 0 " + str(w) + " " + str(h) + "\n")
