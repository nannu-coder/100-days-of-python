height = input('Enter Your Height in m:')
weight = input('Enter Your Weight in kg:')

bmi = int(weight) / float(height)**2

bmi_in_int = int(bmi)

print(bmi_in_int)
