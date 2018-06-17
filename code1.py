"""
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 401
y_pad = 252
Play area =  x_pad+1, y_pad+1, 1138,
"""
"""
Plate coordinates
25 163
127 159
230 156
328 157
427 154
530 156
"""
from PIL import ImageGrab
import os
import time
import win32api, win32con
from PIL import Image,ImageOps
from numpy import *



#Globals
x_pad=340
y_pad=270


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left Release')
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def getcords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)
                          
def screenGrab():
    box = (x_pad+1,y_pad+1,798+x_pad,601+y_pad)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__'+str(int(time.time()))+'.png','PNG')
    return (im)

def startGame():
    #location of sound
    mousePos((254,316))
    leftClick()
    time.sleep(.1)
    
    #location of first menu
    mousePos((256, 154))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((270, 334))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((517, 403))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((254, 324))
    leftClick()
    time.sleep(.1)

    

class Cord:
    f_shrimp = (-26,276)
    f_rice = (36,278)
    f_nori = (-28,329)
    f_roe = (22,340)
    f_salmon = (-25 ,388)
    f_unagi = (21, 386)
#---------------
    phone=(519,300)

    menu_toppings=(472,223)
    t_shrimp=(437,170)
    t_nori=(430,218)
    t_roe=(510,216)
    t_salmon=(508,226)
    t_unagi=(511,170)
    t_exit=(518,291)

    menu_rice=(478,238)
    buy_rice=(478,229)

    delivery_norm=(432,244)

"""25 163
127 159
230 156
328 157
427 154
530 156"""

def clear_tables():
    mousePos((23,158))
    leftClick()
    
 
    mousePos((127,159))
    leftClick()
    
    mousePos((230,156))
    leftClick()
    
    mousePos((328,157))
    leftClick()
    
    mousePos((427,154))
    leftClick()
    
    mousePos((530,156))
    leftClick()
    time.sleep(1)

'''
Recipes:
 
    onigiri
        2 rice, 1 nori
     
    caliroll:
        1 rice, 1 nori, 1 roe
         
    gunkan:
        1 rice, 1 nori, 2 roe
'''
def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if (food == 'caliroll'):
        print ('Making a caliroll')
        foodOnHand['rice']-=1
        foodOnHand['nori']-=1
        foodOnHand['roe']-=1
    
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)
     
    elif (food == 'onigiri'):
        print ('Making a onigiri')
        foodOnHand['rice']-=2
        foodOnHand['nori']-=1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(.05)
        
        time.sleep(1.5)
 
    elif (food == 'gunkan'):
        print('making a gunkan')
        foodOnHand['rice']-=1
        foodOnHand['nori']-=1
        foodOnHand['roe']-=2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)

def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (238,219,169):
            print ('rice is available')
            time.sleep(0.1)
            mousePos(Cord.buy_rice)
            time.sleep(0.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice']+=10
            time.sleep(.1)
            leftClick()
            time.sleep(3)
            
        else:
            print ('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
 
             
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.05)
        if s.getpixel(Cord.t_nori) != (225,181,105):
            print ('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.05)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori']+=10
            time.sleep(.05)
            leftClick()
            time.sleep(3)
        else:
            print ('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(0.5)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftClick()
        s = screenGrab() 
        time.sleep(1)
        if s.getpixel(Cord.t_roe) != (88,68,57):
            print ('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(0.05)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe']+=10
            time.sleep(0.05)
            leftClick()
            time.sleep(.05)
        else:
            print ('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def checkFood():
    for i,j in foodOnHand.items():
        if i=='nori' or i=='rice' or i=='roe':
            if j<=4:
                print('%s is low and needs to be replenished'%i)
                buyFood(i)

                
def get_seat_one():
    box = (378+10+10,346,378+10+10+21,346+24)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return (int(a))
    
def get_seat_two():
    box = (504+10+10,346,504+10+21+10,346+24)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return (int(a))
 
def get_seat_three():
    box = (628+3+10+10,346,628+21+10+10+3,346+24)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return (int(a))
 
def get_seat_four():
    box = (754+10+10+3,346,754+10+3+21+10,346+24)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return (int(a))
 
def get_seat_five():
    box = (880+3+10+10,346,880+10+3+21+10,346+24)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return (int(a))
 
def get_seat_six():
    box = (1006+3+10+10,346,1006+10+3+10+21,346+24)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return (int(a))
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()
    
sushiTypes = {1340:'onigiri', 
              1984:'caliroll',
              1347:'gunkan',}

class Blank:
    seat_1 = 2265
    seat_2 = 3321
    seat_3 = 8781
    seat_4 = 5131
    seat_5 = 1888
    seat_6 = 6972
def check_bubs():
 
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes.keys():
            print ('table 1 is occupied and needs %s' % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print ('sushi not found!\n sushiType = %i' % s1)
 
    else:
        print ('Table 1 unoccupied')
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes.keys():
            print ('table 2 is occupied and needs %s' % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print ('sushi not found!\n sushiType = %i' % s2)
 
    else:
        print ('Table 2 unoccupied')
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes.keys():
            print ('table 3 is occupied and needs %s' % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print ('sushi not found!\n sushiType = %i' % s3)
 
    else:
        print ('Table 3 unoccupied')
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes.keys():
            print ('table 4 is occupied and needs %s' % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print ('sushi not found!\n sushiType = %i' % s4)
 
    else:
        print ('Table 4 unoccupied')
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes.keys():
            print ('table 5 is occupied and needs %s' % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print ('sushi not found!\n sushiType = %i' % s5)
 
    else:
        print ('Table 5 unoccupied')
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes.keys():
            print ('table 1 is occupied and needs %s' % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print ('sushi not found!\n sushiType = %i' % s6)
 
    else:
        print ('Table 6 unoccupied')
 
    clear_tables()
    

def main():
    pass
 
def nigga():
    startGame()
    while True:
        check_bubs()



if __name__== '__main__':
    main()
