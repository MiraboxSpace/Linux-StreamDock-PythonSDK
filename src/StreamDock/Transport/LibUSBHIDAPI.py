import os
import ctypes
import ctypes.util
import platform

arch = platform.architecture()[0]
# If on ARM architecture
if 'arm' in platform.system().lower():
    dll_name = 'libtransport_arm64.so'  # Adjust the library name for ARM
else:
    dll_name = 'libtransport.so'
    
dllabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name
my_transpoet_lib = ctypes.CDLL(dllabspath)

class LibUSBHIDAPI:

    class hid_device_info(ctypes.Structure):
        """
        Structure definition for the hid_device_info structure defined
        in the LibUSB HIDAPI library API.
        """
        pass

    hid_device_info._fields_ = [
        ('path', ctypes.c_char_p),
        ('vendor_id', ctypes.c_ushort),
        ('product_id', ctypes.c_ushort),
        ('serial_number', ctypes.c_wchar_p),
        ('release_number', ctypes.c_ushort),
        ('manufacturer_string', ctypes.c_wchar_p),
        ('product_string', ctypes.c_wchar_p),
        ('usage_page', ctypes.c_ushort),
        ('usage', ctypes.c_ushort),
        ('interface_number', ctypes.c_int),
        ('next', ctypes.POINTER(hid_device_info))
    ]


    my_transpoet_lib.TranSpoet_open_.restype = ctypes.c_int
    my_transpoet_lib.TranSpoet_open_.argtypes= [ctypes.c_void_p,ctypes.c_char_p]

    my_transpoet_lib.TranSport_new.restype=ctypes.c_void_p
    my_transpoet_lib.TranSport_new.argtypes=[]

    my_transpoet_lib.TranSpoet_setBrightness.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_setBrightness.argtypes=[ctypes.c_void_p,ctypes.c_int]

    my_transpoet_lib.TranSpoet_enumerate.restype=ctypes.POINTER(hid_device_info)
    my_transpoet_lib.TranSpoet_enumerate.argtypes=[ctypes.c_void_p,ctypes.c_ushort, ctypes.c_ushort]

    my_transpoet_lib.TranSpoet_getInputReport.restype=ctypes.c_char_p
    my_transpoet_lib.TranSpoet_getInputReport.argtypes=[ctypes.c_void_p,ctypes.c_int]

    my_transpoet_lib.TranSpoet_read.restype=ctypes.c_char_p
    my_transpoet_lib.TranSpoet_read.argtypes=[ctypes.c_void_p]
    
    my_transpoet_lib.TranSpoet_write.restype=ctypes.POINTER(ctypes.c_char)
    my_transpoet_lib.TranSpoet_write.argtypes=[ctypes.c_void_p,ctypes.POINTER(ctypes.c_char),ctypes.c_size_t]
    
    my_transpoet_lib.TranSpoet_freeEnumerate.restype=None
    my_transpoet_lib.TranSpoet_freeEnumerate.argtypes=[ctypes.c_void_p,ctypes.c_void_p]
    
    
    my_transpoet_lib.TranSpoet_setBrightness.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_setBrightness.argtypes=[ctypes.c_void_p,ctypes.c_int]
    
    my_transpoet_lib.TranSpoet_setBackgroundImg.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_setBackgroundImg.argtypes=[ctypes.c_void_p,ctypes.POINTER(ctypes.c_char),ctypes.c_size_t]
    
    my_transpoet_lib.TranSpoet_setKeyImg.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_setKeyImg.argtypes=[ctypes.c_void_p,ctypes.c_char_p,ctypes.c_int]

    my_transpoet_lib.TranSpoet_setKeyImgdata.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_setKeyImgdata.argtypes=[ctypes.c_void_p,ctypes.POINTER(ctypes.c_char),ctypes.c_int,ctypes.c_int,ctypes.c_int]
    
    my_transpoet_lib.TranSpoet_keyClear.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_keyClear.argtypes=[ctypes.c_void_p,ctypes.c_int]
    
    my_transpoet_lib.TranSpoet_keyAllClear.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_keyAllClear.argtypes=[ctypes.c_void_p]

    my_transpoet_lib.TranSpoet_wakeScreen.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_wakeScreen.argtypes=[ctypes.c_void_p]

    my_transpoet_lib.TranSpoet_refresh.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_refresh.argtypes=[ctypes.c_void_p]

    my_transpoet_lib.TranSpoet_disconnected.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_disconnected.argtypes=[ctypes.c_void_p]

    my_transpoet_lib.TranSpoet_close.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_close.argtypes=[ctypes.c_void_p]

    my_transpoet_lib.TranSpoet_screenOff.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_screenOff.argtypes=[ctypes.c_void_p]

    my_transpoet_lib.TranSpoet_screenOn.restype=ctypes.c_int
    my_transpoet_lib.TranSpoet_screenOn.argtypes=[ctypes.c_void_p]
    def __init__(self):
        self.transport=my_transpoet_lib.TranSport_new()


    def open(self,path):
        return my_transpoet_lib.TranSpoet_open_(self.transport,path)
    

    def getInputReport(self,lenth):
        return my_transpoet_lib.TranSpoet_getInputReport(self.transport,lenth)
    
    def read(self):
        arr= my_transpoet_lib.TranSpoet_read(self.transport)

        return arr

    def wirte(self,data,lenth):
        return my_transpoet_lib.TranSpoet_write(self.transport,data,lenth)
    
    def freeEnumerate(self,devs):
        my_transpoet_lib.TranSpoet_freeEnumerate(self.transport,devs)

    def enumerate(self,vid,pid):
        
        vendor_id = vid or 0
        product_id = pid or 0
        device_list = []
        device_enumeration = my_transpoet_lib.TranSpoet_enumerate(self.transport,vendor_id,product_id)
        if device_enumeration:
            current_device = device_enumeration
            while current_device:
                device_list.append({
                    'path': current_device.contents.path.decode('utf-8'),
                    'vendor_id': current_device.contents.vendor_id,
                    'product_id': current_device.contents.product_id,
                })
                current_device = current_device.contents.next
        self.freeEnumerate(device_enumeration)
        return device_list


    def setBrightness(self,percent):
        return my_transpoet_lib.TranSpoet_setBrightness(self.transport,percent)
    
    def setBackgroundImg(self,buffer,size):
        return my_transpoet_lib.TranSpoet_setBackgroundImg(self.transport,buffer,size)
    
    def setKeyImg(self,path,key):
        return my_transpoet_lib.TranSpoet_setKeyImg(self.transport,path,key)
        
    def setKeyImgdata(self,imagedata,key,width,height):
        return my_transpoet_lib.TranSpoet_setKeyImgdata(self.transport,imagedata,key,width,height)
    
    def keyClear(self,index):
        return my_transpoet_lib.TranSpoet_keyClear(self.transport,index)
    
    def keyAllClear(self):
        return my_transpoet_lib.TranSpoet_keyAllClear(self.transport)
    
    def wakeScreen(self):
        return my_transpoet_lib.TranSpoet_wakeScreen(self.transport)
    
    def refresh(self):
        return my_transpoet_lib.TranSpoet_refresh(self.transport)
    
    def disconnected(self):
        return my_transpoet_lib.TranSpoet_disconnected(self.transport)
    
    def close(self):
        return my_transpoet_lib.TranSpoet_close(self.transport)
    
    def screen_Off(self):
        return my_transpoet_lib.TranSpoet_screenOff(self.transport)
    def screen_On(self):
        return my_transpoet_lib.TranSpoet_screenOn(self.transport)