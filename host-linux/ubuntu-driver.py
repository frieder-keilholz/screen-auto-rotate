#!/usr/bin/env python3

import serial
import subprocess

def main():
    print("Start Serial")
    s = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=None)
    s.flush()
    current_orientation = 0
    #select display
    screen = subprocess.check_output("xrandr | grep ' connected' | cut -d ' ' -f1", shell=True).decode().strip()
    print(screen)

    try:
        while True:
            mes = s.readline().decode()
            #print(mes)
            if mes == "1\r\n":
                if current_orientation != 1:
                    current_orientation = 1
                    #change screen orientation to horizontal
                    subprocess.call(f"xrandr --output {screen} --rotate normal", shell=True) #(customize rotation here)

            elif mes == "2\r\n":
                if current_orientation != 2:
                    current_orientation = 2
                    #change screen orientation to vertical
                    subprocess.call(f"xrandr --output {screen} --rotate left", shell=True) #(customize rotation here)
                    
    except KeyboardInterrupt:
        s.close()

if __name__ == "__main__":
    main()