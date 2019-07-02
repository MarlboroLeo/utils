# coding=utf-8
# @Time    : 2019/7/2 15:08
# @Author  : Leau
# @File    : tesseract_handle_cap_unfinish.py
import cv2 as cv
from PIL import Image
import pytesseract


def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 6))
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 1))
    open_out = cv.morphologyEx(binl, cv.MORPH_OPEN, kernel)
    cv.bitwise_not(open_out, open_out)  # 背景变为白色
    cv.imshow("转换", open_out)
    textImage = Image.fromarray(open_out)
    text = pytesseract.image_to_string(textImage)
    print("This OK:%s" % text)


src = cv.imread("./tst.jpg")
cv.imshow("原来", src)
recognize_text()
cv.waitKey(0)