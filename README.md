pos_img_train.py -> generates positive cropped images and stores them in the folder, "positive_images"

makeposfile.py -> creates info1.dat file

neg_img.py -> file to read negative images and store them in the folder, "negative_images", also creates bg1_orig.txt
	      
testing_cars.py -> file to test the classifier on test images and detect if cars are present or not.

haar_training -> folder containing the cascade.xml after training HAAR classifier using opencv_traincascade application
LBP_training -> folder containing the cascade.xml after training LBP classifier using opencv_traincascade application

info1.dat -> contains the filenames of all the cropped positive images, along with the number of object instances and the dimensions of the object bounded rectangle

bg1_orig.txt -> contains the absolute path of all the negative images.

Once you generate info1.dat and bg1_orig.txt, make sure you place them in "positive_images" and "negative_images", respectively.

Note: I executed makeposfile.py, neg_img.py and pos_img_train.py on Windows, and not on the docker image, because to execute those Python files, I had to move the positive and negative images onto the docker image. But when I moved them all to the docker image, Pycharm failed to open and it became really slow and laggy.



Refer the report for more details.
