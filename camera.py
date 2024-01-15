import cv2
import time

# 打开摄像头
cap = cv2.VideoCapture(0)

# 设置摄像头参数（可选）
cap.set(cv2.CAP_PROP_FPS, 30)  # 帧率为 30 帧/秒

while True:
    # 读取摄像头图像
    ret, frame = cap.read()

    # 转换为灰度图像
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 显示图像
    cv2.imshow('frame', frame)

    # 等待 1 秒
    #time.sleep(1)

    # 检测是否按下了 q 键，如果是则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()