import cv2 as cv
import time

camera_device = 0
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break

    cv.imshow("Video", frame)

    # MÃ ASCII CỦA PHÍM ESC
    # NHẤN PHÍM ESC ĐỂ THOÁT
    key = cv.waitKey(10)

    if key == 27:
        break

    # KIEM TRA NEU SAVE THI LUU TEN FILE THEO THANG NGAY NAM GIO PHUT GIAY HIEN TAI
    if key == ord('s') or key == ord('S'):
        t = time.localtime()
        fileName = 'image_%04d_%02d_%02d_%02d_%02d_%02d.jpg' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
        cv.imwrite(fileName, frame)
