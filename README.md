# screen-auto-rotate
Automatic adjustment to your screen orientation when turning your screen.

### Sensor
A Hall effect sensor connected to a Raspberry Pi Pico is used to detect the display's orientation.

### Host Connection
The Host is connected via USB and orientation changes are transmitted over serial.

### Host Driver
A Python script receives the changes and adjusts the screen orientation between landscape and portrait mode.
