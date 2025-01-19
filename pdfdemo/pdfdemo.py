import pdf2image
import cv2 as cv
import numpy as np

def main():
    # 画像抽出用PDFを取得
    print("Hello")
    pdfimages = pdf2image.convert_from_path("etude1-4.pdf")
    cvimage = np.asarray(pdfimages[0]).copy()

    thresh = cv.rectangle(cvimage,(384,0),(510,128),(0,255,0),3)
    # ret, thresh = cv.threshold(cvimage, 127,255, cv.THRESH_BINARY_INV)
    cv.imshow("pdf2image sample", thresh)
    cv.waitKey(0)

if __name__ == '__main__':
    main()