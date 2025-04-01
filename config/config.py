class Config:
    LEFT_PIC_PATH = ''
    RIGHT_PIC_PATH = ''
    MAP_X_PATH = ''
    MAP_Y_PATH = ''
    RIGHT_CENTRE = ""
    RIGHT_ZERO_POINT = ""
    RIGHT_180_POINT = ""
    RIGHT_90_POINT = ""
    LEFT_CENTRE = ""
    LEFT_ZERO_POINT = ""
    LEFT_180_POINT = ""
    LEFT_90_POINT = ""


# 像素点配置
Config.VERSION = 1

if Config.VERSION == 1:
    Config.RIGHT_CENTRE = (155, 351)
    Config.RIGHT_ZERO_POINT = (166, 63)
    Config.RIGHT_180_POINT = (142, 650)
    Config.RIGHT_90_POINT = (551, 349)

    Config.LEFT_CENTRE = (461, 340)
    Config.LEFT_ZERO_POINT = (474, 44)
    Config.LEFT_180_POINT = (457, 637)
    Config.LEFT_90_POINT = (89, 353)

# 路径配置
Config.LEFT_PIC_PATH = '../pic/left1.jpg'
Config.RIGHT_PIC_PATH = '../pic/right1.jpg'
Config.MAP_X_PATH = "../Distortion/mapx.npy"
Config.MAP_Y_PATH = "../Distortion/mapy.npy"