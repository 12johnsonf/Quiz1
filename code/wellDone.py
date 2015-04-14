import time
import ctypes
def congrats(score,n):
    print("Score: ", score)
    if score > 6:
        ctypes.windll.user32.MessageBoxW(0, "Congratulations "+n, "Well done", 0)
