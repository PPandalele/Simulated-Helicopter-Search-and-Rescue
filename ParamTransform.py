from config.config import Config
from Lib.Pix import Pix
import math


class ParamTransform:
    """参数转换"""
    right_hand_center_point = Config.RIGHT_CENTRE      # 右机械手中心点
    right_hand_zero_point = Config.RIGHT_ZERO_POINT      # 右机械手基点
    right_hand_180_point = Config.RIGHT_180_POINT
    left_hand_center_point = Config.LEFT_CENTRE
    left_hand_zero_point = Config.LEFT_ZERO_POINT
    left_hand_180_point = Config.LEFT_180_POINT
    pix = Pix()

    def right_windows(self, x: int, y: int):
        """
        右边窗口参数转换z
        :param x:  x坐标
        :param y:  y 坐标
        :return:   angle_pwm length_pwm
        """
        # 360°舵机转的角度
        k_x, k_y = 0.087, 0.118
        pix_angle_0 = self.pix.angle((x, y), self.right_hand_center_point, self.right_hand_zero_point, k_x, k_y)
        if pix_angle_0 <= 90:
            front_or_back = "front"
            # pix_angle = pix_angle_0
            pix_angle = self.get_angle_coefficient(pix_angle_0, "right_and_front")
        else:
            k_x, k_y = 0.093, 0.123
            pix_angle_0 = self.pix.angle((x, y), self.right_hand_center_point, self.right_hand_180_point, k_x, k_y)
            front_or_back = "back"
            # pix_angle = pix_angle_0
            pix_angle = self.get_angle_coefficient(pix_angle_0, "right_and_back")
        if self.clicked_right_or_left((x, y), "right", front_or_back) == "left":
            print("do not clicked on left")
            return False
        # 720°舵机转的角度
        physical_length = self.pix_to_real_length((x, y), self.right_hand_center_point, k_x, k_y)
        length_angle = self.physical_length_to_angle(physical_length)
        if self.right_angle2pwm_720(length_angle, front_or_back) is False:
            print("out of range")
            return False
        print("right：" + str(pix_angle_0) + " (" + front_or_back + ")")
        print("right：" + str(length_angle))
        return self.right_angle2pwm_360(pix_angle, front_or_back), self.right_angle2pwm_720(length_angle, front_or_back)

    def left_windows(self, x: int, y: int):
        """
        右边窗口参数转换
        :param x:  x坐标
        :param y:  y 坐标
        :return:   angle_pwm length_pwm
        """
        # 360°舵机转的角度
        k_x, k_y = 0.096, 0.116
        pix_angle_0 = self.pix.angle((x, y), self.left_hand_center_point, self.left_hand_zero_point, k_x, k_y)
        if pix_angle_0 <= 90:
            front_or_back = "front"
            # pix_angle = pix_angle_0
            pix_angle = self.get_angle_coefficient(pix_angle_0, "left_and_front")
        else:
            k_x, k_y = 0.102, 0.124
            pix_angle_0 = self.pix.angle((x, y), self.left_hand_center_point, self.left_hand_180_point, k_x, k_y)
            front_or_back = "back"
            # pix_angle = pix_angle_0
            pix_angle = self.get_angle_coefficient(pix_angle_0, "left_and_back")
        if self.clicked_right_or_left((x, y), "left", front_or_back) == "right":
            print("do not clicked on right")
            return False
        # 720°舵机转的角度
        physical_length = self.pix_to_real_length((x, y), self.left_hand_center_point, k_x, k_y)
        length_angle = self.physical_length_to_angle(physical_length)
        if self.left_angle2pwm_720(length_angle, front_or_back) is False:
            print("out of range")
            return False
        print("left：" + str(pix_angle_0) + " (" + front_or_back + ")")
        print("left：" + str(length_angle))
        return self.left_angle2pwm_360(pix_angle, front_or_back), self.left_angle2pwm_720(length_angle, front_or_back)

    @staticmethod
    def get_angle_coefficient(angle, right_or_left_and_front_or_back: str):
        """
        360舵机角度系数
        angle = real_angle * k + b
        """
        if right_or_left_and_front_or_back == "right_and_front":
            angle_1, real_angle_1 = 23.267, 21.393
            angle_2, real_angle_2 = 63.030, 60.483
        elif right_or_left_and_front_or_back == "right_and_back":
            angle_1, real_angle_1 = 28.633, 29.885
            angle_2, real_angle_2 = 73.368, 82.137
        elif right_or_left_and_front_or_back == "left_and_front":
            angle_1, real_angle_1 = 28.270, 32.820
            angle_2, real_angle_2 = 66.934, 75.089
        else:
            angle_1, real_angle_1 = 19.713, 21.123
            angle_2, real_angle_2 = 57.108, 59.579
        k = (angle_1 - angle_2) / (real_angle_1 - real_angle_2)
        b = angle_1 - real_angle_1 * k
        angle = k * angle + b
        return angle

    @staticmethod
    def pix_to_real_length(click_point: tuple, hand_point: tuple, k_x: float, k_y: float):
        """像素长度转换成物理长度"""
        real_length = math.sqrt(math.pow(math.fabs(click_point[0] - hand_point[0])*k_x, 2)
                                + math.pow(math.fabs(click_point[1] - hand_point[1])*k_y, 2))
        return real_length

    @staticmethod
    def physical_length_to_angle(length):
        circumference = 35.5     # cm
        k = 360 / circumference
        return length * k

    def clicked_right_or_left(self, clicked_point: tuple, right_or_left_window: str, front_or_back: str)->str:
        """判断鼠标点击在中心线的左边还是右边"""
        if right_or_left_window == "right":
            if front_or_back == "front":
                centre, base = self.right_hand_center_point, self.right_hand_zero_point
            else:
                centre, base = self.right_hand_center_point, self.right_hand_180_point
        else:
            if front_or_back == "front":
                centre, base = self.left_hand_center_point, self.left_hand_zero_point
            else:
                centre, base = self.left_hand_center_point, self.left_hand_180_point
        k, b = self.pix.get_equation(centre, base)
        if k >= 0:
            return "left" if clicked_point[1] >= clicked_point[0] * k + b else "right"
        else:
            return "right" if clicked_point[1] >= clicked_point[0] * k + b else "left"

    @staticmethod
    def right_angle2pwm_360(angle, front_or_back: str):
        """int(angle / 90.0 + 1.0) * 500.0 + 1500"""
        if front_or_back == "front":
            pwm = 1550 + angle * 2000 / 360
        else:
            pwm = 1550 - angle * 2000 / 360
        # 不足四位补零
        pwm = str(round(pwm))
        pwm = '0' * (4 - len(pwm)) + pwm
        return pwm

    @staticmethod
    def left_angle2pwm_360(angle, front_or_back: str):
        """int(angle / 90.0 + 1.0) * 500.0 + 1500"""
        if front_or_back == "front":
            pwm = 1550 - angle * 2000 / 360
        else:
            pwm = 1550 + angle * 2000 / 360
        # 不足四位补零
        pwm = str(round(pwm))
        pwm = '0' * (4 - len(pwm)) + pwm
        return pwm

    @staticmethod
    def right_angle2pwm_720(length_angle, front_or_back: str):
        """int(angle / 90.0 + 1.0) * 500.0 + 1500"""
        if front_or_back == "front":
            pwm = 1500 - length_angle * 2000 / 720
        else:
            pwm = 1500 + length_angle * 2000 / 720
        if pwm < 500 or pwm > 2500:
            return False
        # 不足四位补零
        pwm = str(round(pwm))
        pwm = '0'*(4-len(pwm)) + pwm
        return pwm

    @staticmethod
    def left_angle2pwm_720(length_angle, front_or_back: str):
        """int(angle / 90.0 + 1.0) * 500.0 + 1500"""
        if front_or_back == "front":
            pwm = 1500 - length_angle * 2000 / 720
        else:
            pwm = 1500 + length_angle * 2000 / 720
        if pwm < 500 or pwm > 2500:
            return False
        # 不足四位补零
        pwm = str(round(pwm))
        pwm = '0'*(4-len(pwm)) + pwm
        return pwm


if __name__ == '__main__':
    # print(ParamTransform.get_length((1, 1), (2, 2)))
    p = ParamTransform()
    # res = p.pix_to_real_length((0, 46), "left")
    # print(res)
