A public infrastructure has various parking lots. The parking lots get completely occupied very
often and the public visiting the infrastructure spend too much time looking for a parking space,
unaware that the parking lot is completely occupied. They would like to implement an automated
solution to convey this information by displaying the number of available parking spaces at the
entrance to the parking lot.

These parking lots are overlooked be surveillance cameras. The task is to leverage them to detect
and count the empty parking spots. 

I've described each file content's within this repository below:

* pos_img_train.py -> generates positive cropped images and stores them in the folder, "positive_images"

* makeposfile.py -> creates info1.dat file

* neg_img.py -> file to read negative images and store them in the folder, "negative_images", also creates bg1_orig.txt
	      
* testing_cars.py -> file to test the classifier on test images and detect if cars are present or not.

* haar_training -> folder containing the cascade.xml after training HAAR classifier using opencv_traincascade application

* LBP_training -> folder containing the cascade.xml after training LBP classifier using opencv_traincascade application

* info1.dat -> contains the filenames of all the cropped positive images, along with the number of object instances and the dimensions of the object bounded rectangle

* bg1_orig.txt -> contains the absolute path of all the negative images.

Once you generate info1.dat and bg1_orig.txt, make sure you place them in "positive_images" and "negative_images", respectively.


Refer the report for more details.
