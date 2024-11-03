import ctypes
import time
import os
import subprocess
from playsound import playsound

def get_current_background():
    # استرجاع الخلفية الحالية
    SPI_GETDESKWALLPAPER = 0x0073
    buffer_size = 512
    wallpaper_path = ctypes.create_unicode_buffer(buffer_size)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, buffer_size, wallpaper_path, 0)
    return wallpaper_path.value

def change_background(image_path):
    # تغيير الخلفية
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

def scary_message():
    # رسالة التخويف
    ctypes.windll.user32.MessageBoxW(
        0,
        "تحذير! تم اكتشاف نشاط مشبوه على جهازك!\n"
        "سيتم إيقاف تشغيل النظام لحماية بياناتك...",
        "تنبيه أمني",
        0x10 | 0x1
    )

def play_scary_sound():
    # تشغيل الصوت المخيف
    sound_path = r"C:\Path\To\Scary\Music.mp3"
    playsound(sound_path)

def restart_computer():
    # إعادة التشغيل بعد 15 ثانية
    subprocess.run("shutdown /r /t 15", shell=True)

if __name__ == "__main__":
    # استرجاع الخلفية الأصلية
    original_image_path = get_current_background()
    
    # مسار صورة المقلب
    prank_image_path = r"C:\Path\To\اختراق وايفايات\Imag.jpeg"
    
    # تغيير الخلفية للصورة الجديدة
    change_background(prank_image_path)
    
    # تشغيل الصوت المخيف
    play_scary_sound()
    
    # عرض رسالة التخويف
    scary_message()
    
    # انتظار 15 ثانية ثم إعادة التشغيل
    time.sleep(15)
    restart_computer()

    # بعد إعادة التشغيل، يمكنك إعادة الخلفية الأصلية
    change_background(original_image_path)