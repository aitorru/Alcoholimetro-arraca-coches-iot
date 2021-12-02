#!/usr/bin/python

import time, sys
from grove.adc import ADC
from grove.grove_led import GroveLed

class CustomAlcoholSensor(object):
    # Pass the channel that the sensor is connected to.
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
    
    @property
    def value(self):
        RS_air = 33.0
        ratio = 0.0
        sensorValue = 0.0
        for i in range(1000):
            sensorValue = sensorValue + float(self.adc.read(self.channel))
        sensorValue = sensorValue / 1000.0
        sensorVolt = sensorValue/1024*5.0
        RS_gas = float(sensorVolt/(5.0 - sensorVolt))
        print("RS_gas: {}".format(RS_gas))
        ratio = RS_gas/RS_air

        return ratio

def main():
    sensor  = CustomAlcoholSensor(2)
    led     = GroveLed(5)
    print("Reading")

    while True:
        value = sensor.value
        print(value)
        if (value <= 0.01):
            led.on()
        else:
            led.off()
        time.sleep(1)

if __name__ == '__main__':
    main()
