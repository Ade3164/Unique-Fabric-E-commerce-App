from PIL import ImageGrab
import numpy as np
from PIL import ImageGrab
import cv2
from win32api import GetSystemMetrics
import datetime

print('Adebayo camcoder')
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

vid_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
vid_name = f'{vid_time}.mp4'

webcam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter(vid_name, fourcc, 20.0, (width, height))
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_last = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    ar_ar, frame = webcam.read()
    fr_height, fr_width, ar = frame.shape
    img_last[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]
    
    cv2.imshow('secret capture', img_last)
    #cv2.imshow('webcam', frame)
    capture_video.write(img_last)
    if cv2.waitKey(10) == ord('q'):
        break