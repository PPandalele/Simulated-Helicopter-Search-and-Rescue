import math


class Pix:
    """图像坐标计系算工具类"""

    @staticmethod
    def get_equation(point_1: tuple, point_2: tuple):
        """
        返回头像坐标系两点确定的直线方程的斜率和常数项
        :param point_1:
        :param point_2:
        :return:  斜率k 和 常数项b
        """
        k = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
        b = point_1[1] - point_1[0] * k
        return k, b

    @staticmethod
    def length(point_1: tuple, point_2: tuple, k_x: float, k_y: float):
        """计算图像坐标系上两点的距离"""
        return math.sqrt(math.pow(math.fabs(point_1[0] - point_2[0]) * k_x, 2)
                         + math.pow(math.fabs(point_1[1] - point_2[1]) * k_y, 2))

    def angle(self, input_point: tuple, center_point: tuple, base_point: tuple, k_x: float, k_y: float):
        """
        计算图像坐标系上的角度， 利用余弦定理
        cos a =  ( ab^2 +ac^2 - bc^2 ) / 2*ab*ac
        :param input_point:  输入的点
        :param center_point:    中心点
        :param base_point:      基点
        :param k_x:
        :param k_y:
        :return:
        """
        a = center_point
        b = base_point
        c = input_point
        ab = self.length(a, b, k_x, k_y)
        ac = self.length(a, c, k_x, k_y)
        bc = self.length(b, c, k_x, k_y)
        cos_a = (ab*ab + ac*ac - bc*bc) / (2*ab*ac)
        # 反余弦得出角度
        res = math.degrees(math.acos(cos_a))
        return res
        # return round(res, 3)


if __name__ == '__main__':
    p = Pix()
    # l = p.length((471, 256), (483, 63))
    # print(l)
