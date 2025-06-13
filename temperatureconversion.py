def main(): 
    print("Welcome to the Celsius/Farenheit converter!")
    converter = input("What would you like to convert to? Write 'c' for Celsius and 'f' for Farenheit.\n")
    temperature = int(input(f"What is the temperature to convert to {converter}?\n"))
    if converter == 'c': 
        #convert to celsius 
        Celsius = convertToCelsius(temperature)
        print(f'The temperature in degrees Celsius is {Celsius}.')

    elif converter == 'f':
        #convert to Farenheit 
        Fahrenheit = convertToFahrenheit(temperature)
        print(f'The temperature in degrees Fahrenheit is {Fahrenheit}')

    else: 
        print("Please indicate which unit of measure to convert to.")
        converter = input("What would you like to convert to? Write 'c' for Celsius and 'f' for Farenheit")


def convertToFahrenheit(degreesCelsius): 
    #convert from Celsius to Farenheit
    Farenheit = degreesCelsius*(9/5)+32 
    return Farenheit 

def convertToCelsius(degreesFahrenheit): 
    #convert from Farenheit to Celsius 
    Celsius = (degreesFahrenheit - 32)*(5/9)
    return Celsius

assert convertToCelsius(0) == -17.77777777777778

assert convertToCelsius(180) == 82.22222222222223

assert convertToFahrenheit(0) == 32

assert convertToFahrenheit(100) == 212

assert convertToCelsius(convertToFahrenheit(15)) == 15

if __name__ == "__main__": 
    main()