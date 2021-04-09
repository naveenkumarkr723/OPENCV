# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:36:59 2020

@author: jadin
"""


import cv2

def main():
    
    imgpath=r"C:\Users\jadin\Downloads\standard_test_images\lena_co6.4.1.01.tiff"
    img=cv2.imread(imgpath)
    cv2.imshow("nan",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__=="__main__":
    main()