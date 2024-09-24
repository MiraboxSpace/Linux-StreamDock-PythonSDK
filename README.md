# Linux Systems (Ubuntu/Debian)

You need to install `pillow`, `pyudev`, `threading`, `ctypes`, `time`, `abc`

```bash
pip install pillow
```
```bash
pip install pyudev
```
```bash
pip install threading
```
```bash
pip install ctypes
```
```bash
pip install time
```
```bash
pip install abc
```

When using it, you need to first define a `DeviceManager` class object (device manager class), and then call its `enumerate()` function to traverse the devices and obtain a list of device objects.

```py
manner = DeviceManager();
streamdocks = manner.enumerate();
```

After obtaining the list of device objects, you need to call the `open()` method to open the device before calling other methods to operate on the device.

```py
 for device in streamdocks:
    device.open()
    device.refresh()
    t1 = threading.Thread(target=device.whileread)
    t1.start()
    # 0-100
    device.set_brightness(100)
    device.set_touchscreen_image("1.jpg")
    time.sleep(1)
    device.set_key_image(3, "2.jpg")
    time.sleep(1)
    device.cleaerIcon(3)
    time.sleep(1)
    device.clearAllIcon()
    device.refresh()
    time.sleep(1)
    device.close()
    time.sleep(1)
```

Please see the [document](https://creator.key123.vip/en/linux/python/dependency.html) for details