


import cv2
cap = cv2.VideoCapture(0)


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(r'C:\Users\jadin\Downloads\misc.avi',fourcc, 30.0, (640,480))

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        out.write(frame)
        cv2.imshow('naveen_video_saving',frame)
        
        if cv2.waitKey(1) == 27:
            break
       

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()