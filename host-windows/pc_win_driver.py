import serial
import rotatescreen

def main():
    print("Start Serial")
    s = serial.Serial(port="COM9", baudrate=9600, timeout=None)
    s.flush()
    current_orientation = 0
    #device = win32.EnumDisplayDevices(None,0)
    #print("[%d] %s (%s)"%(0,device.DeviceString,device.DeviceName))
    #device = win32.EnumDisplayDevices(None,1)
    #print("[%d] %s (%s)"%(1,device.DeviceString,device.DeviceName))
    screen = rotatescreen.get_secondary_displays()[0]
    print(screen)

    try:
        while True:
            mes = s.readline().decode()
            #print(mes)
            if mes == "1\r\n":
                if current_orientation != 1:
                    #print("change screen orientation to horizontal")
                    current_orientation = 1
                    #change screen orientation to horizontal
                    screen.set_landscape()

            elif mes == "2\r\n":
                if current_orientation != 2:
                    #print("change screen orientation to vertical")
                    current_orientation = 2
                    #change screen orientation to vertical
                    screen.set_portrait_flipped()
                    
    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    main()