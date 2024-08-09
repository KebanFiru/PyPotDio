from Com import arduino
from pynput.keyboard import Key, Controller

keyboard = Controller()

voice_level = []

def keypress(key):
    keyboard.press(key)
    keyboard.release(key) 

def main_func():
    try:
        arduino.open()
        arduino.readline()
        while arduino:
            value = arduino.readline().decode('utf-8')  
            print(value)      
            try:
                if value not in voice_level:
                    voice_level.append(int(value.strip()))
                    if int(value) > voice_level[0] :
                        keypress(Key.media_volume_up)
                        voice_level.clear()
                        voice_level.append(int(value.strip()))
                    elif int(value) < voice_level[0]:
                        keypress(Key.media_volume_down)
                        voice_level.clear()
                        voice_level.append(int(value.strip()))
            except:
                pass
    except:
        print("An error occured")
main_func()