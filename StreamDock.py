from abc import ABCMeta, abstractmethod
import ctypes
import ctypes.util
class StreamDock():
    transport=None
    __metaclass__ = ABCMeta    
    def __init__(self,transport1,devInfo):
        self.transport=transport1
        self.vendor_id=devInfo['vendor_id']
        self.product_id=devInfo['product_id']
        self.path=devInfo['path']
    # 打开设备
    def open(self):
        self.transport.open(bytes(self.path,'utf-8'))
    # 关闭设备
    def close(self):
        self.disconnected()
        # self.transport.close()
    # 断开连接清楚所有显示
    def disconnected(self):
        self.transport.disconnected()
    # 清除某个按键的图标
    def cleaerIcon(self,index):
        self.transport.keyClear(index)
    # 清除所有按键的图标
    def clearAllIcon(self):
        self.transport.keyAllClear()
    # 唤醒屏幕
    def wakeScreen(self):
        self.transport.wakeScreen()
    # 刷新设备显示
    def refresh(self):
        self.transport.refresh()
    # 获取设备路径
    def getPath(self):
        return self.path
    # 获取设备反馈的信息
    def read(self):
        """
        :argtypes:存放信息的字节数组，字节数组的长度建议512

        """
        arr=self.transport.read()
        return arr
    # 一直检测设备有无信息反馈，建议开线程使用
    def whileread(self):
        while 1:
            arr=self.read()
            if len(arr)>=10:
                if arr[9]==0xFF:
                    print("写入成功")
                else:
                    print("按键{}".format(arr[9]))
                    if arr[10]==0x01:
                        print("被按下")
                    else:
                        print("抬起")
            else:
                print(arr)
            del arr

    @abstractmethod
    def get_serial_number(self):
        pass


    @abstractmethod
    def set_key_image(self, key, image):
        pass

    @abstractmethod
    def set_key_imagedata(self, key, image,width=126,height=126):
        pass


    @abstractmethod
    def set_brightness(self, percent):
        pass

    @abstractmethod
    def set_touchscreen_image(self, image):
        pass