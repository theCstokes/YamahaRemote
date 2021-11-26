import serial 
pump = serial.Serial(port = 'COM1', baudrate = 9600)

if(pump.cts == False):
    while(True):
        raw_input('Please connect your null modem cable to your Yamaha receiverand and press enter.')
        pump.open()

def enter():
    print('Enter')
    pump.write(b'@SYS:REMOTECODE=7A85DE21\r\n')

def left():
    print('Left')
    pump.write(b'@SYS:REMOTECODE=7A859F60\r\n')

def right():
    print('Right')
    pump.write(b'@SYS:REMOTECODE=7A859E61\r\n')

def up():
    print('Up')
    pump.write(b'@SYS:REMOTECODE=7A859D62\r\n')

def down():
    print('Down')
    pump.write(b'@SYS:REMOTECODE=7A859C63\r\n')

def back():
    print('Back')
    pump.write(b'@SYS:REMOTECODE=7A85AA55\r\n')

def onscreen():
    print('Show On Screen Menu')
    pump.write(b'@SYS:REMOTECODE=7A85847B\r\n')

def volUp():
    print('Volume Up')
    pump.write(b'@SYS:REMOTECODE=7A851AE5\r\n')

def volDown():
    print('Volume Down')
    pump.write(b'@SYS:REMOTECODE=7A851BE4\r\n')

import getch
from msvcrt import getch
while True:
    print("Action (press h for help): ")
    key = ord(getch())
    # print(key)
    if key == 27: #ESC
        print('Hasta lasagna don\'t get any on ya')
        break
    elif key == 61: #VolUp
        volUp()
    elif key == 45: #VolDown
        volDown()
    elif key == 104: #Enter
        print('s will bring up on screen')
        print('backspace will go back')
        print('arrow keys will navigate')
        print('enter keys will select current option')
        print('plus/minus keys will chnage the volume')
        print('Esc will exit')
    elif key == 13: #Enter
        enter()
    elif key == 8: #Back
        back()
    elif key == 115: #Enter
        onscreen()
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            down()
        elif key == 72: #Up arrow
            up()
        if key == 77: #Right arrow
            right()
        elif key == 75: #Left arrow
            left()

# while(True):
#     val = raw_input('Action: ')

#     if (val == 'enter'):
#         enter()
#     elif (val == 'left'):
#         left()
#     elif (val == 'right'):
#         right()
#     elif (val == 'up'):
#         up()
#     elif (val == 'down'):
#         down()
#     elif (val == 'back'):
#         back()
#     elif (val == 'onscreen'):
#         onscreen()
#     elif(val == 'exit'):
#         quit()
#     elif(val == 'quit'):
#         quit()


