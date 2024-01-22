import serial
import rotatescreen

def main():
    print("Start Serial")
    s = serial.Serial(port="COM9", baudrate=9600, timeout=None) #(customize COM Port here)
    s.flush()
    current_orientation = 0
    screen = rotatescreen.get_secondary_displays()[0]
    print(screen)

    try:
        while True:
            mes = s.readline().decode()
            #print(mes)
            if mes == "1\r\n":
                if current_orientation != 1:
                    current_orientation = 1
                    #change screen orientation to horizontal
                    screen.set_landscape() #(customize here)

            elif mes == "2\r\n":
                if current_orientation != 2:
                    current_orientation = 2
                    #change screen orientation to vertical
                    screen.set_portrait_flipped() #(customize here)
                    
    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    main()