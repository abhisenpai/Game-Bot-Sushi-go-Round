from PIL import ImageGrab
import os
import time

#Globals
"""x_pad=341
y_pad=272
"""
def screenGrab():
    box = ()
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__'+str(int(time.time()))+'.png','PNG')

def main():
    screenGrab()

if __name__== '__main__':
    main()
    

"""
1st top 375,346

2nd top 501,346
3rd top 628,346
4th top 754,346
5th top 880,346
6th top 1006,346
"""
