def conversion():
    unit = input("What unit are you using for temperature? (kelvin, celsius, fahrenheit): ").strip().lower()
    while unit not in ["kelvin", "celsius", "fahrenheit"]:
        unit = input("Please type a correct unit. (kelvin, celsius, fahrenheit): ")
    converted_unit = input("What unit do you want to convert to? (kelvin, celsius, fahrenheit): ").strip().lower()
    while converted_unit not in ["kelvin", "celsius", "fahrenheit"]:
        converted_unit = input("Please type a correct unit. (kelvin, celsius, fahrenheit): ")
    try:
        temperature = float(input("What is the temperature value? "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")
        return

    if unit == "kelvin":
        if converted_unit == "kelvin":
            print(f"{temperature} kelvin.")
        elif converted_unit == "celsius":
            print(f"{temperature - 273.15:.2f} celsius.")
        elif converted_unit == "fahrenheit":
            print(f"{(temperature - 273.15) * 1.8 + 32:.2f} fahrenheit.")
        else:
            print("Unsupported conversion unit.")
    elif unit == "celsius":
        if converted_unit == "kelvin":
            print(f"{temperature + 273.15:.2f} kelvin.")
        elif converted_unit == "celsius":
            print(f"{temperature} celsius.")
        elif converted_unit == "fahrenheit":
            print(f"{temperature * 1.8 + 32:.2f} fahrenheit.")
        else:
            print("Unsupported conversion unit.")
    elif unit == "fahrenheit":
        if converted_unit == "kelvin":
            print(f"{(temperature - 32) * 5 / 9 + 273.15:.2f} kelvin.")
        elif converted_unit == "celsius":
            print(f"{(temperature - 32) * 5 / 9:.2f} celsius.")
        elif converted_unit == "fahrenheit":
            print(f"{temperature} fahrenheit.")
        else:
            print("Unsupported conversion unit.")
    else:
        print("Unsupported temperature unit.")

if __name__ == "__main__":
    conversion()