number =  float(input("Enter the value:"))
choice = input("The valus is in Celsius? c: Fahrenheit: f")

if choice == 'c':
    fahrenheit=(number*1.8)+32
    print('Fahrenheit value is:', fahrenheit)
if choice=='f':
    celsius=(number-32)*5/9
    print('Celsius value is:',celsius)