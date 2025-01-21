import pdf2image
import cv2 as cv
import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas

def main():
    # 画像抽出用PDFを取得
    print("Hello")
    pdfimages = pdf2image.convert_from_path("etude1-4.pdf")
    cvimage = np.asarray(pdfimages[0]).copy()

    font = cv.FONT_HERSHEY_SIMPLEX
    thresh = cv.putText(cvimage,'OpenCV',(150,150), font, 4,(0,255,0),2,cv.LINE_AA)
    # ret, thresh = cv.threshold(cvimage, 127,255, cv.THRESH_BINARY_INV)
    cv.imshow("pdf2image sample", thresh)
    cv.waitKey(0)

    cv.imwrite("output.png", cvimage)

    image = Image.open("output.png")
    width, height = image.size

    c = canvas.Canvas("outputpdf.pdf", pagesize=(width, height))

    c.drawImage("output.png", 0, 0, width, height)
    c.showPage()
    c.save()

if __name__ == '__main__':
    main()