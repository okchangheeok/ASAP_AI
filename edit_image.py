from PIL import Image
from io import BytesIO
import cv2
import numpy as np

<<<<<<< HEAD
def add_images(text_img,bg_img):
    text_img, bg_img = list(map(lambda img:np.array(img),[text_img,bg_img]))
    ## 마스크 생성
    gray = cv2.cvtColor(text_img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    mask = cv2.bitwise_not(mask)

    src, dst = text_img, bg_img
    img_result = cv2.copyTo(src, mask, dst)
    img_result = cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB)
=======
def add_images(img1,img2):
    img1,img2=tuple(map(lambda img:np.array(img),[img1,img2]))
    img_result=cv2.add(img1,img2)
>>>>>>> parent of 2cff95d ([feat] develop module to add two images)
    img_bytes = cv2.imencode('.jpg', img_result)[1].tobytes()
    return img_bytes