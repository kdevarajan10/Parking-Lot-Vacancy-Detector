import cv2
import xml.etree.ElementTree as ET
import os
import sys
import argparse

def model_test(img, xmlfilename, detector, scaleFactor, minNeighbors):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = detector.detectMultiScale(img_gray, scaleFactor, minNeighbors, maxSize=(100, 100), minSize=(20, 20))

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    parking_occ = 0
    parking_emp = 0
    true_positives = 0
    false_positives = 0
    coordinates = dict()

    tree = ET.parse(xmlfilename)
    e = tree.getroot()
    for space in e.findall('space'):
        id = space.get('id')
        occupied = space.get('occupied')
        if occupied == '1':
            parking_occ = parking_occ + 1
        else:
            parking_emp = parking_emp + 1

        coordinates[id] = []
        for point in space.iter('point'):
            x = point.attrib.get('x')
            y = point.attrib.get('y')
            coordinates[id].append((x, y))
        x1 = [int(x) for (x, y) in coordinates[id]]
        y1 = [int(y) for (x, y) in coordinates[id]]
        x_mid = (min(x1) + max(x1)) / 2
        y_mid = (min(y1) + max(y1)) / 2
        for (cx, cy, w, h) in cars:
            if cx < x_mid and x_mid < (cx + w) and cy < y_mid and y_mid < (cy + h) and occupied == '1':
                true_positives = true_positives + 1
                break
            elif cx < x_mid and x_mid < (cx + w) and cy < y_mid and y_mid < (cy + h) and occupied == '0':
                false_positives = false_positives + 1
                break

    false_negatives = parking_occ - true_positives
    true_negatives = parking_emp - false_positives

    accuracy = ((true_positives + true_negatives) / (parking_occ + parking_emp)) * 100

    print("The number of parking spots that are filled = ", parking_occ)
    print("The number of parking spots that are empty = ", parking_emp)
    print("------------------------------------------------------")
    print("The number of True Positives = ", true_positives)
    print("The number of False Positives = ", false_positives)
    print("The number of True Negatives = ", true_negatives)
    print("The number of False Negatives = ", false_negatives)
    print("\n")
    print("Accuracy = ", accuracy)
    print("\n\n")

    return (img)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-img", "--imgPath", dest="imgPath", help="Specify the path to the image", required=True)
    parser.add_argument("-ft", "--featureType", dest="featureType",
                        help="Specify the feature type of the classifier to be used (HAAR - HAAR Classifier,  LBP - Local Binary Pattern Classifier)", required=True,
                        type=str, choices=['HAAR', 'LBP'])
    parser.add_argument("-sf", "--scaleFactor", dest="scaleFactor",
                        help="Specify the scale factor to be used for detection ",
                        type=float, required=True)
    parser.add_argument("-mn", "--minimumNeighbors", dest="minNeighbors",
                        help="Specify the minimum number of neighbours present for individual detection to be considered ",
                        type=int, required=True)

    args = parser.parse_args()

    img = cv2.imread(args.imgPath)
    if img is None:
        print("ERROR: The path to the image is incorrect. Please try again")
        sys.exit()
    else:
        output = os.path.splitext(args.imgPath)[0] + args.featureType + "_output.jpg"
        xmlfilename = os.path.splitext(args.imgPath)[0] + ".xml"
        print("-------------------------------------")
        print("Image Filename: ", args.imgPath)
        print("-------------------------------------")

    if args.featureType == 'HAAR':
        detector = cv2.CascadeClassifier("haar_training/cascade.xml")
        result = model_test(img, xmlfilename, detector, args.scaleFactor, args.minNeighbors)
        cv2.imwrite(output, result)

    if args.featureType == 'LBP':
        detector = cv2.CascadeClassifier("LBP_training/cascade.xml")
        result = model_test(img, xmlfilename, detector, args.scaleFactor, args.minNeighbors)
        cv2.imwrite(output, result)


if __name__ == "__main__":
    main()
