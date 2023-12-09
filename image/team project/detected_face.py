import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('웹캠 캡쳐 화면.jpg')
faces = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    print(f"Detected face position: x={x}, y={y}, width={w}, height={h}")

cv2.imshow('얼굴감지', img)
cv2.waitKey(0)
cv2.destroyAllWindows()