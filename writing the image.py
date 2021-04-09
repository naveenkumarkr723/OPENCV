# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 19:37:54 2020

@author: jadin
"""

import cv2

def main():
    
    
    window_name = "writing_image"
    
    img_path = r"C:\Users\jadin\Downloads\misc\misc\5.1.10.tiff"
    
    img = cv2.imread(img_path,1)
    
    out_path = r"C:\Users\jadin\Documents\open_cv\5.1.10.jpg"
    
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    
    cv2.imshow(window_name, img)
    
    k = cv2.waitKey(0)                    
    
    if k== 27: # wait for ESC key to exit
        cv2.destroyAllWindows()
        
        
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(out_path,img)
        cv2.destroyAllWindows()

    else:
        pass
    
    
    
    
if __name__=="__main__":
    main()
    
    
