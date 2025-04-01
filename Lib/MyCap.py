import cv2
from config.config import Config
from Lib.MyDraw import DrawPic
from Distortion.Distortion import Distortion
from PyQt5.QtCore import pyqtSignal, QThread


class MyCap(QThread):
    """摄像头开启线程"""
    posSignal = pyqtSignal(str, int, int, str)   # 点击坐标信号x ,y
    distortion = Distortion()   # 去畸变
    draw = DrawPic()    # 画线描点

    def __init__(self):
        super(QThread, self).__init__()
        self.left_cap = None
        self.right_cap = None
        self.clicked_point = {
            "right": [],
            "left": []
        }

    def set(self, left_cap, right_cap):
        """设置摄像源"""
        self.left_cap = left_cap
        self.right_cap = right_cap

    def run(self):
        """读取摄像头，并且显示"""
        self.two_cap_start()
        # self.single_cap_test_run(self.left_cap)

    def two_cap_start(self):
        """双摄像头启动"""
        print("cap run......")
        cv2.namedWindow("RightWindow")
        cv2.namedWindow("LeftWindow")
        cv2.setMouseCallback("LeftWindow", self.mouse_callback_left)
        cv2.setMouseCallback("RightWindow", self.mouse_callback_right)
        while True:
            try:
                self.left_cap.saveSnapshot(Config.LEFT_PIC_PATH)
                self.right_cap.saveSnapshot(Config.RIGHT_PIC_PATH)
                left_img = cv2.imread(Config.LEFT_PIC_PATH)[0:480, 0:720]
                right_img = cv2.imread(Config.RIGHT_PIC_PATH)[0:480, 0:720]
                left_img, right_img = self.distortion(left_img, right_img)
                self.draw(left_img, right_img, self.clicked_point)
                cv2.imshow("RightWindow", right_img)
                cv2.imshow("LeftWindow", left_img)
                c = cv2.waitKey(1) & 0xff
                if c == 27:
                    break
            except Exception as e:
                print(str(e))
                print("cap run error")
                break

    def single_cap_test_run(self, cap):
        """单个摄像头测试"""
        print("single_cap run......")
        cv2.namedWindow("LeftWindow")
        cv2.setMouseCallback("LeftWindow", self.mouse_callback_left)
        while True:
            cap.saveSnapshot('../pic/cap_pic.jpg')
            frame = cv2.imread('../pic/cap_pic.jpg')
            cv2.imshow("LeftWindow", frame)
            c = cv2.waitKey(1) & 0xff
            if c == 27:
                break

    def mouse_callback_left(self, event, x, y, *_):
        """左窗口绑定函数"""
        # print("mouse_callback_left--->x:{0},y:{1}", format(str(x), str(y)))
        if event == cv2.EVENT_LBUTTONDOWN:
            self.posSignal.emit("left", x, y, "catch")
            self.clicked_point["left"].append((x, y))
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.posSignal.emit("left", x, y, "back")
        elif event == cv2.EVENT_MBUTTONDOWN:
            self.posSignal.emit("left", -255, -255, "back")
            self.clicked_point["left"].clear()
            self.clicked_point["right"].clear()

    def mouse_callback_right(self, event, x, y, *_):
        """右窗口绑定函数"""
        if event == cv2.EVENT_LBUTTONDOWN:
            self.posSignal.emit("right", x, y, "catch")
            self.clicked_point["right"].append((x, y))
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.posSignal.emit("right", x, y, "back")
        elif event == cv2.EVENT_MBUTTONDOWN:
            self.posSignal.emit("right", -255, -255, "back")
            self.clicked_point["right"].clear()
            self.clicked_point["left"].clear()
