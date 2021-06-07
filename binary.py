import os, sys
import cv2

def convert_to_binary(img_grayscale, thresh=100):
    thresh, img_binary = cv2.threshold(img_grayscale, thresh, maxval=255, type=cv2.THRESH_BINARY)
    return img_binary
def to_result(input_image_path):
    img_grayscale = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    img_binary = convert_to_binary(img_grayscale, thresh=100)
    cv2.imwrite('binary_%s' % input_image_path, img_binary)
    print('Saved binary image @ result_%s' % input_image_path)
# Cách dùng