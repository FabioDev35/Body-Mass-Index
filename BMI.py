import time
nome = str(input('Write your name: '))
altura = float(input('Write your height in meters (eg. 1.80): '))
peso = float(input('Write your weight in kg: '))
imc = peso / (altura * altura)

if (imc < 17):
    print('Hi {}, your BMI is {:.2f}, therefore you are very underweight!'.format(nome,imc))
elif (imc <= 18.49):
    print('Hi {}, your BMI is {:.2f}, therefore you are underweight!'.format(nome,imc))
elif (imc <= 24.99):
    print('Hi {}, your BMI is {:.2f}, therefore your weight is normal!'.format(nome,imc))
elif (imc <= 29.99):
    print('Hi {}, your BMI is {:.2f}, therefore you are overweight!'.format(nome,imc))
elif (imc <= 34.99):
    print('Hi {}, your BMI is {:.2f}, therefore you are Obese (Class I)!'.format(nome,imc))
elif (imc <= 39.99):
    print('Hi {}, your BMI is {:.2f}, therefore you are Obese (Class II)!'.format(nome,imc))
elif (imc > 40):
    print('Hi {}, your BMI is {:.2f}, therefore you are Obese (Class III)!'.format(nome,imc))

time.sleep(10)