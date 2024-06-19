def convert_temp(temp, unit1, unit2):
    if unit1  == "C" and unit2 == "F":
        return (temp * 9/5) + 32
    elif unit1 == "F" and unit2 == "C":
        return ((temp - 32) * 5/9)
    else:
        return "Invalid units"

temp_1 = int(input("Enter the value of temperature"))
unit_1 = input("Enter the unit of the temperature (C for celcius , F for fahrenheit): ")
unit_2 = input("Enter the unit of the temperature you want to convert: ")

print("After conversion the value of temperature is: ", convert_temp(temp_1,unit_1,unit_2))
