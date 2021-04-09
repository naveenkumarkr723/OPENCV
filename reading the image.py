
import cv2


def main():
    print("naveen kumar")
    
    img_path = r"C:\Users\jadin\Downloads\misc\misc\5.1.10.tiff"
    
    ### here 0 =grey_scale,1=rgb_scale
    img = cv2.imread(img_path,1)
    
    
    ### see what actually a img looklikes
    
    print(img)
    print(type(img))
    
    ### saving the  image 
    cv2.imwrite(r"C:\Users\jadin\Documents\open_cv",img)
    
    
    ### first is the window name
    cv2.imshow("first",img)
    

    
    ### these two  are compulsary
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    
   
    
if __name__ == "__main__" :
    main()
    
"""cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyWindow('first')"""
        
    
"""cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for
specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is passed,
it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which
we will discuss below""",


"""cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window,
use the function cv2.destroyWindow() where you pass the exact window name as the argument."""    
    