# Tính BMI (Chỉ số khối cơ thể)

urweight = float(input("Enter your weight(kg): "))
urheight = float(input("Enter your height(m): "))
bmi = urweight / (urheight * urheight)
print(f"Your BMI is {bmi:.2f}")