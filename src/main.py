from StreamDock.DeviceManager import DeviceManager
from StreamDock.ImageHelpers import PILHelper
import threading
import time

if __name__ == "__main__":
    manner=DeviceManager()
    # 监听设备插拔
    t = threading.Thread(target=manner.listen)
    t.start()
    streamdocks= manner.enumerate()
    print("Found {} Stream Dock(s).\n".format(len(streamdocks)))
    for device in streamdocks:
        # 打开设备
        device.open()
        # 开线程获取设备反馈
        t1= threading.Thread(target=device.whileread)
        t1.start()
        # 设置设备亮度0-100
        device.set_brightness(100)
        # 设置背景图片（传图片的地址）
        device.set_touchscreen_image("1.jpg")
        time.sleep(1)
        # # 设置设备某个按键的图标
        device.set_key_image(3,  "2.jpg")
        time.sleep(1)
        # 清空某个按键的图标
        device.cleaerIcon(3)
        time.sleep(1)
        # # 清空所有按键的图标
        device.clearAllIcon()
        # # 刷新显示屏
        device.refresh()
        time.sleep(1)
        # # 关闭设备
        device.close()
        time.sleep(1)

    t.join()
    t1.join()