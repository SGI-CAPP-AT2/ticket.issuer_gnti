"""
Simple Initial code written by Shubham Ingale
Ref: GFG
This code has no sense respecting the project
// A code with Decimal to Binary Converter
"""
import machine
LEDs = [5,18,19,21,32]
LED_Objects=[]
for i in LEDs:
    print(i)
    LED_Objects.append(machine.Pin(i, machine.Pin.OUT))
    print(i)
ErrorLed = LED_Objects[4];
def changeStateOfLeds(n):
    arr=list(map(int, str(n)))
    if(len(arr)<4):
       for i in range(4-len(arr)):
           arr.insert(0, 0)
    for j in range(len(arr)):
        LED_Objects[j].value(arr[j]);
        print(arr[j])
def decimalToBinary(n):
    return "{0:b}".format(int(n))
def binary(n):
    ErrorLed.off()
    if n < 16:
        changeStateOfLeds(decimalToBinary(n));
    else:
        ErrorLed.on();