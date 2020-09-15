import cv2

#open video file
cap = cv2.VideoCapture('video/myatnoe.mp4')
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(str(i)+'.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()