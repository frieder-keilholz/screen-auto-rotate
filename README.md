# screen-auto-rotate
Automatic adjustment to your screen orientation when turning your screen.

### Sensor
A Hall effect sensor connected to a Raspberry Pi Pico is used to detect the display's orientation.

### Host Connection
The Host is connected via USB and orientation changes are transmitted over serial.

### Host Driver
A Python script receives the changes and adjusts the screen orientation between landscape and portrait mode.

## Requirements
On the Host install python packages:
- rotate-screen
- pyserial

## Install
1) Adjust your Analog Pin in the main.py file
2) Copy the main.py file to your Raspberry Pico
3) Connect the Pi to the Host PC and note down the COM port
4) Adjust the COM port as well as screen and screen orientation (portrait_flipped/portrait) in the pc_win_driver.py 
5) Run Windows+R and enter shell:startup then create a link to win_auto_start.vbs to have it autostart on boot
