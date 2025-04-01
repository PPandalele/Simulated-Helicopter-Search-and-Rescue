import numpy as np
import cv2
from config.config import Config


class Distortion:
    """去畸变"""
    map_x = np.load(Config.MAP_X_PATH)
    map_y = np.load(Config.MAP_Y_PATH)

    def __call__(self, left_pic, right_pic, *args, **kwargs):
        left_res = cv2.remap(left_pic, self.map_x, self.map_y, cv2.INTER_LINEAR)[50:400, 130:390, :]
        right_res = cv2.remap(right_pic, self.map_x, self.map_y, cv2.INTER_LINEAR)[50:400, 130:390, :]
        left_res, right_res = cv2.resize(left_res, (640, 700)), cv2.resize(right_res, (640, 700))  # (700, 480)
        left_res = self.rotate(left_res, 270)
        right_res = self.rotate(right_res, 90)
        return left_res, right_res

    def rotate(self, image, angle, center=None, scale=1.0):
        # 获取图像尺寸
        (h, w) = image.shape[:2]
        # 若未指定旋转中心，则将图像中心设为旋转中心
        if center is None:
            center = (w / 2, h / 2)
        # 执行旋转
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(image, M, (w, h))
        # 返回旋转后的图像
        return rotated

