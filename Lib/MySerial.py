import serial


class MySerial:
    """ 向电控串口发送信息"""
    obj = None

    @classmethod
    def set(cls, port: str, baudrate: int):
        if cls.obj:
            cls.obj.close()
        cls.obj = serial.Serial(timeout=0.5)
        cls.obj.port = port
        cls.obj.baudrate = baudrate
        cls.obj.open()

    @classmethod
    def send(cls, msg: str):
        if not cls.obj:
            raise EOFError("Port and baudrate have not set!")
        cls.obj.write(msg.encode())


if __name__ == '__main__':
    # MySerial.set("com1", 9600)
    MySerial.send("test")


