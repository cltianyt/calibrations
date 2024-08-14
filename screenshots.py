import cv2
import time

# 摄像头IP地址
camera_ips = [
    'rtsp://admin:KaiHong%40123@10.70.1.139:5543/Streaming/Channels/101',
    'rtsp://admin:KaiHong@123@10.70.1.139:5545/stream',
    'rtsp://admin:KaiHong%40123@10.70.1.139:5531/Streaming/Channels/101'
]

# 保存路径模板
save_path_template = r'C:\\Users\\kaihong\\Desktop\\Calibration-ZhangZhengyou-Method (2)\\Calibration-ZhangZhengyou-Method\\chessing_board\\pic_{}.jpg'

# 初始化视频捕捉对象
caps = [cv2.VideoCapture(ip) for ip in camera_ips]

# 给摄像头一些时间来初始化
time.sleep(2)

# 读取每个摄像头的一帧
frames = []
for i, cap in enumerate(caps):
    ret, frame = cap.read()
    if ret:
        frames.append(frame)
        save_path = save_path_template.format(i)
        cv2.imwrite(save_path, frame)
        print(f'Frame from camera {i} saved to {save_path}')
    else:
        print(f'Failed to capture frame from camera {i}')

# 释放所有视频捕捉对象
for cap in caps:
    cap.release()

cv2.destroyAllWindows()
