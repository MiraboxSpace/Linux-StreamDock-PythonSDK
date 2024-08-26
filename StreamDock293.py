from StreamDock import StreamDock
from PIL import Image
import ctypes
import ctypes.util
import os
class StreamDock293(StreamDock):


    def __init__(self, transport1, devInfo):
        super().__init__(transport1, devInfo)

    # 设置设备的屏幕亮度
    def set_brightness(self, percent):
        return self.transport.setBrightness(percent)
    

    # 设置设备的背景图片
    def set_touchscreen_image(self, image):

        image = Image.open(image)
        # 转换为RGB模式
        image = image.convert('RGB')
        width,height=image.size
        # 获取图片的像素数据
        pixels = list(image.getdata())

        bgr_data = []
    
        # 遍历像素数据，将RGB值转换为BGR值并添加到列表中
        for pixel in pixels:
            r, g, b = pixel
            bgr_data.extend([r, g, b])
        arr_type = ctypes.c_char * len(bgr_data)
        arr_ctypes = arr_type(*bgr_data)
        reversed_bgr_array = arr_ctypes[::-1]
        return self.transport.setBackgroundImg(reversed_bgr_array,width*height*3)
    
    # 设置设备的按键图标
    def set_key_image(self, image, key):
        # 打开图片
        image1 = Image.open(image)

        # 旋转图片180度
        rotated_image = image1.rotate(180)

        # 保存旋转后的图片
        rotated_image.save("Temporary.jpg","JPEG")
        returnvalue = self.transport.setKeyImg(bytes("Temporary.jpg",'utf-8'), key)
        os.remove("Temporary.jpg")
        return returnvalue
    

    # 获取设备的固件版本号
    def get_serial_number(self,lenth):
        return self.transport.getInputReport(lenth)