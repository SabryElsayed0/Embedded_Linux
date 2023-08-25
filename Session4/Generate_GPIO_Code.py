# Write python codeto generate Initfunction of GPIOfor AVR
import os
DDR = ["0b"]
for i in range(0,8):
    bit = input(f"please enter Bit {i} mode : ")
    if bit == "in":
        DDR.append('1')
    elif bit == "out":
        DDR.append('0')
        
bits ="".join(DDR)
print(bits)

GpioInit = 'void Gpio_Init void \n\
{\n \
        DDR ='+ bits  + ';\n'\
    +'}\n \
                    '
    
with open("GPIO.c",'w') as GPIO:
    GPIO.write(GpioInit)