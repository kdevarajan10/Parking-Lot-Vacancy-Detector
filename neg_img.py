import cv2
import glob

ctr = 0
for filename in glob.iglob("E:\\HW1\\cv-homework-3-kdevarajan10\\256_ObjectCategories\\*\\*.jpg", recursive=True):
    img = cv2.imread(filename)
    resize_img = cv2.resize(img, (100, 100), interpolation=cv2.INTER_AREA)
    cv2.imwrite("E:\\HW1\\cv-homework-3-kdevarajan10\\negative_images\\neg_img" + str(ctr) + ".jpg", resize_img)
    ctr = ctr + 1

f = open("bg.txt", 'w')

for filename in glob.iglob('negative_images\\*.jpg', recursive=True):
    img = cv2.imread(filename)
    f.write(filename + "\n")
