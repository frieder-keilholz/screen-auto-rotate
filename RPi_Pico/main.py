from machine import Pin, ADC, UART
import time

#uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
#uart.init(bits=8, parity=None, stop=2)
hall_sensor = ADC(Pin(28))
print("START_")

while True:
    # read analog sensor
    reading = hall_sensor.read_u16()

    # delay 1 second
    if(reading < 51500):
        #uart.write("Orientation A\n")
        #print(1)
        #print('\n')
        print("1")
    elif(reading > 53000):
        print(2)
        #uart.write("Orientation B\n")
    #else:
        #print(" ")
    time.sleep(0.5)