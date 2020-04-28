import cv2
facecascade=cv2.CascadeClassifier('D:\\faceRecognition-master\\haarcascade_frontalface.xml')
videocapt=cv2.VideoCapture(0)
while True:
    retval,frame=videocapt.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(35,35))
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,200,50),2)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        sys.exit()
