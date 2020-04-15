import cv2
import glob
f = open("info.dat", 'w')

for filename in glob.glob('positive_images\\*.jpg'):
    img = cv2.imread(filename)
    h = img.shape[0]
    w = img.shape[1]

    f.write(filename + " 1 0 0 " + str(w) + " " + str(h) + "\n")
