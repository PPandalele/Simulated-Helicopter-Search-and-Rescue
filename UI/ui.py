from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from UI.contral_state import Ui_MainWindow
from Lib.MySerial import MySerial
from Lib.MyCap import MyCap
from VideoCapture import Device
from ParamTransform import ParamTransform
import sys

from config.config import Config


class ControlWindow(QMainWindow, Ui_MainWindow):

    serial = MySerial
    cap_thread = MyCap()
    paramTransform = ParamTransform()
    right_cap = None
    left_cap = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 标志变量
        self.is_open_cap = False
        # 额外UI设置
        self.setFixedSize(self.width(), self.height())  # 禁止缩放
        self.setWindowIcon(QIcon('icon.png'))
        self.com.addItem("com9")    # 增加com选项
        self.com.setCurrentIndex(2)     # 设置默认com
        self.baudrate.setCurrentIndex(2)  # 设置默认baudrate
        self.openButton.hide()
        self.swapButton.hide()
        # 槽函数绑定
        self.set_button.clicked.connect(self.set_serial)
        self.openButton.clicked.connect(self.open_cap)
        self.openButton.clicked.connect(self.change_sheet)
        self.swapButton.clicked.connect(self.swap_cap)
        self.cap_thread.posSignal.connect(self.pos_msg_update)

    def set_serial(self):
        """setButton槽函数，设置serial"""
        try:
            port = self.com.currentText()
            baudrate = self.baudrate.currentText()
            self.serial.set(port, baudrate)
        except:
            return
        self.__msg_print("com", "设置串口")
        self.__msg_print("com", "串口com--->{0}".format(port))
        self.__msg_print("com", "波特率--->{0}".format(baudrate))
        self.__msg_print("com", "---------------------")
        self.set_button.setDisabled(True)
        self.openButton.show()
        self.swapButton.show()

    def open_cap(self):
        """openButton槽函数，开始读取摄像头"""
        self.left_cap = Device(devnum=2)
        self.right_cap = Device(devnum=0)
        # self.left_cap = None
        # self.right_cap = None
        self.cap_thread.set(self.left_cap, self.right_cap)
        # 线程
        self.cap_thread.start()

    def swap_cap(self):
        """左右摄像头交换"""
        self.left_cap, self.right_cap = self.right_cap, self.left_cap
        self.cap_thread.set(self.left_cap, self.right_cap)

    def change_sheet(self):
        """button改变样式"""
        style_sheeet = "background-color:  rgb(0, 101, 127);\ncolor: rgb(255, 255, 255);" if not self.is_open_cap else \
            "background-color: rgb(0, 191, 243);\ncolor: rgb(255, 255, 255);"
        self.is_open_cap = not self.is_open_cap
        self.openButton.setStyleSheet(style_sheeet)

    def __msg_print(self, obj, msg):
        """根据obj，往不同信息栏写入信息"""
        if obj == "com":    # 串口信息栏
            self.comBrowser.append("<font color='green'>"+msg + '</font>')
        elif obj == "left":     # 左边信息栏
            self.leftBrowser.append(msg)
        elif obj == "right":    # 右边信息栏
            self.rightBrowser.append(msg)

    def pos_msg_update(self, right_or_left, x, y, mode):
        """接收信号，更新坐标信息"""
        # print("pos_msg_update --> x:{0},y:{1}", format(x, y))
        if x == -255 and y == -255:
            self.serial.send("s15501500c")      # 归中
            print("归中")
        else:
            browser_obj = self.leftBrowser if right_or_left == "left" else self.rightBrowser
            browser_obj.append("x坐标为：{0}，y坐标为{1}".format(str(x), str(y)))
            end = "a" if mode == "catch" else "b"
            res = self.paramTransform.right_windows(x, y) if right_or_left == "right" \
                else self.paramTransform.left_windows(x, y)
            if res:
                angle_pwm, length_pwm = res
                self.serial.send("s{0}{1}{2}".format(angle_pwm, length_pwm, end))
                print("s{0}{1}{2}".format(angle_pwm, length_pwm, end))
            # print(mode)
        # if right_or_left == "right":
        #     angle_pwm, length_pwm = self.paramTransform.right_windows(x, y)
        #     self.serial.send("s{0}{1}a".format(angle_pwm, length_pwm))

    def closeEvent(self, event):
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ControlWindow()
    window.show()
    sys.exit(app.exec_())
