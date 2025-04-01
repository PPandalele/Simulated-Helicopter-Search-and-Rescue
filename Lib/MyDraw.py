import cv2
from config.config import Config


class DrawPic:
    """画图工具类"""
    right_hand_center_point = Config.RIGHT_CENTRE       # 右机械手中心点
    right_hand_zero_point = Config.RIGHT_ZERO_POINT     # 右机械手基点
    right_hand_180_point = Config.RIGHT_180_POINT
    right_hand_90_point = Config.RIGHT_90_POINT
    left_hand_center_point = Config.LEFT_CENTRE
    left_hand_zero_point = Config.LEFT_ZERO_POINT
    left_hand_180_point = Config.LEFT_180_POINT
    left_hand_90_point = Config.LEFT_90_POINT

    # cv2.line(img, point_1, point_2, (255, 0, 255), 1) #  第五个参数粗细
    # cv2.circle(img, center_point, r, (255, 255, 255), 1) 第五个参数粗细，负数表示实心

    def left_img_draw(self, img):
        """左边窗口图像传入"""
        # cv2.circle(img, self.left_hand_center_point, 3, (0, 0, 255), -1)
        # cv2.circle(img, self.left_hand_zero_point, 3, (0, 0, 255), -1)
        # cv2.circle(img, (457, 468), 3, (255, 0, 255), -1)
        cv2.line(img, self.left_hand_center_point, self.left_hand_zero_point, (0, 255, 0), 2)
        cv2.line(img, self.left_hand_center_point, self.left_hand_180_point, (0, 255, 0), 2)
        # cv2.line(img, self.left_hand_center_point, (466, 9), (0, 255, 0), 2)
        # 圆弧, 90-270
        # cv2.ellipse(img, Config.LEFT_CENTRE, (363, 363), 0, 90, 270, (0, 255, 0), 1)
        # cv2.ellipse(img, (533, 337), (402, 308), 0, 90, 270, (255, 255, 255), 1)
        cv2.ellipse(img, self.left_hand_center_point,
                    (self.left_hand_180_point[1] - self.left_hand_center_point[1],
                     self.left_hand_center_point[0] - self.left_hand_90_point[0]),
                    90, 0, 90, (0, 255, 0), 2)
        cv2.ellipse(img, self.left_hand_center_point,
                    (self.left_hand_center_point[1] - self.left_hand_zero_point[1],
                     self.left_hand_center_point[0] - self.left_hand_90_point[0]),
                    90, 90, 180, (0, 255, 0), 2)

        cv2.circle(img, self.left_hand_center_point, 2, (0, 0, 255), 2)
        cv2.circle(img, self.left_hand_zero_point, 2, (0, 0, 255), 2)
        cv2.circle(img, self.left_hand_180_point, 2, (0, 0, 255), 2)

    def right_img_draw(self, img):
        """右边窗口图像传入"""
        # cv2.circle(img, (236, 449), 3, (255, 0, 255), -1)   # 180°点
        cv2.line(img, self.right_hand_center_point, self.right_hand_zero_point, (0, 255, 0), 2)
        cv2.line(img, self.right_hand_center_point, self.right_hand_180_point, (0, 255, 0), 2)
        # cv2.line(img, self.right_hand_center_point, (200, 11), (0, 255, 0), 1)
        # 圆弧, 90-270
        # cv2.ellipse(img, Config.RIGHT_CENTRE, (356, 356), 180, 90, 270, (0, 255, 0), 1)
        # cv2.ellipse(img, (151, 362), (375, 298), 180, 90, 270, (255, 255, 255), 1)
        # cv2.ellipse(img, Config.RIGHT_CENTRE, (282, 282), 180, 90, 270, (0, 255, 0), 1)
        cv2.ellipse(img, self.right_hand_center_point,
                    (self.right_hand_center_point[1] - self.right_hand_zero_point[1],
                     self.right_hand_90_point[0] - self.right_hand_center_point[0]),
                    90, 180, 270, (0, 255, 0), 2)
        cv2.ellipse(img, self.right_hand_center_point,
                    (self.right_hand_180_point[1] - self.right_hand_center_point[1],
                     self.right_hand_90_point[0] - self.right_hand_center_point[0]),
                    90, 270, 360, (0, 255, 0), 2)

        cv2.circle(img, self.right_hand_center_point, 2, (0, 0, 255), 2)
        cv2.circle(img, self.right_hand_zero_point, 2, (0, 0, 255), 2)
        cv2.circle(img, self.right_hand_180_point, 2, (0, 0, 255), 2)

    @staticmethod
    def draw_clicked(left_img, right_img, click_dict: dict):
        """连续点击痕迹"""
#        for point in click_dict["left"]:
#            cv2.circle(left_img, point, 2, (255, 0, 255), -1)
#        for point in click_dict["right"]:
#            cv2.circle(right_img, point, 2, (255, 0, 255), -1)

    def __call__(self, left_img, right_img, click_dict):
        return self.left_img_draw(left_img), self.right_img_draw(right_img),\
               self.draw_clicked(left_img, right_img, click_dict)


if __name__ == '__main__':
    img = cv2.imread("../pic/left.jpg")
    d = DrawPic()
    img = d.left_img_draw(img)
    cv2.imshow("img", img)
    cv2.waitKey(0)
